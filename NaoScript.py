import sys
import os
import csv
import time
import nao2 as n

def FindFile(file_name, sub_dir):
    """Search for a file in the PYTHONPATH/sub_dir and in PYTHONPATH/ directories.
    Return None if not found otherwise return the found path/file_name."""
    list_path = sys.path #the first directory is the current directory
    the_path=None
    file_name=file_name.lstrip("\\/") # remove leading back-/forward slashes
    sub_dir=sub_dir.lstrip("\\/")
    sub_dir=sub_dir.rstrip("\\/")
    for i in range (0,len(list_path)):
        if os.path.exists(list_path[i]+"/"+sub_dir+"/"+file_name):
            the_path=list_path[i]+"/"+sub_dir+"/"+file_name
            break
        if os.path.exists(list_path[i]+"/"+file_name):
            the_path=list_path[i]+"/"+file_name
            break
    return the_path

def FindPath(sub_dir):
    """Search for a file in the PYTHONPATH/sub_dir and in PYTHONPATH/ directories.
    Return None if not found otherwise return the found path/file_name."""
    list_path = sys.path #the first directory is the current directory
    sub_dir=sub_dir.lstrip("\\/")
    sub_dir=sub_dir.rstrip("\\/")
    filefound = False
    for i in range (0,len(list_path)):
        if os.path.exists(list_path[i]+"/"+sub_dir):
            filefound = True
            the_dir=list_path[i]+"/"+sub_dir
            break

    if not filefound:
        print "Could not find "+ sub_dir + " directory!"
        raise IOError
        return None

    return the_dir, os.listdir(the_dir)

def FindExt(file_list, ext_list):
    mylist = []     
    for x in file_list:
        for y in ext_list:
            if x.endswith(y):
                mylist.append(x)
    return mylist


class Nao_Script:
    def __init__(self, nao_interface):
        self.nao=nao_interface
    #######################################################################
    ## This functions executes movements transported from choregraph
    ## and saved in a *.py file. Make sure to initialize the motion proxy.
    #######################################################################
    def RunMovement(self,file_name, post = True, to_start_position = True):
        """ Give up the filename containing the movement. Needs motion proxy."""

        path_name=FindFile(file_name,"gestures")
        if not path_name:
            print "Gesture "+str(path_name)+" not found in PYTHONPATH"
            return

        file_load = open(path_name)
        lines = file_load.readlines()
        for i in range(0,len(lines)):
            if lines[i].startswith("try:"): # When Choregraphe exports movements as Python files, it contains a try-block at the end. This must not be executed.
                break
            exec lines[i]

        if to_start_position:
            last_key = self.nao.motionProxy.getAngles(names, True)

            high_time = 0.0
            for i in range(0,len(times)):
                cur_time = times[i][len(times[i])-1]
                if cur_time > high_time:
                    high_time = cur_time

            for i in range(0, len(times)):
                times[i].append(high_time+0.1)
                times[i].append(high_time+2)
                keys[i].append(keys[i][len(keys[i])-1])
                keys[i].append([last_key[i],[ 3, -0.55556, 0.00000], [ 3, 0.55556, 0.00000]])

        
        if post:
            self.nao.motionProxy.post.angleInterpolationBezier(names, times, keys)
        else:
            self.nao.motionProxy.angleInterpolationBezier(names, times, keys)

    ###########################################################################
    ## This function runs a speech script saves as a *.csv file. Column 1
    ## contains the time in seconds, Column 2 contains the TTS input. This
    ## function requires a TTS proxy.
    ###########################################################################
    def RunSpeech(self,file_name):
        """ file_name is the name containing the speech script."""
        path_name=FindFile(file_name,"tts")

        if not path_name:
            print "Speech file "+str(path_name)+" not found in PYTHONPATH"
            return

        try:
            script_reader = csv.reader(open(path_name, 'rb'))
        except:
            print "Speech script does not exist!!!"
            return
        cur_line = script_reader.next()
        start_time = time.time()
        while True:
            try:
                cur_line = script_reader.next()
            except:
                break
            while float(cur_line[0])> (time()-start_time):
                time.sleep(0.1)
            self.nao.Say(cur_line[1])
            
    ########################################################################
    ## Uses a led CSV file to read out the proper eye pattern variables.
    ## Allows you to set LED Group, RGB, and Duration
    ## Frequency is currently ignored
    ## CSV file format:
    ##  Row 1 = Header (ignored)
    ##  Row 2-n = LED Group; Red; Green; Blue; Frequency; Duration
    ## Duration = Fade Time past to ALLeds.FadeListRGB
    ## CSV file delimiter is ';' (Used by Excel)
    #########################################################################
    def RunLED(self,file_name, post = True):
        """ Uses a led CSV file to read out the proper eye pattern variables."""
        #open CSV file
        path_name=FindFile(file_name,"led")

        if not path_name:
            print "LED file "+str(path_name)+" not found in PYTHONPATH"
            return
         
        file_load = open(path_name, 'rb')

        #read all rows of CSV file (assumes delimiter is ';')
        csv_reader = csv.reader(file_load, delimiter=';')

        #read header row and ignore it
        csv_reader.next()

        #initialize LEDs to off
        self.nao.ledProxy.post.off('FaceLeds')
        #print 'ledProxy.post.off(', 'FaceLeds', ')'

        #read first LED command and initialize fadeListRGB parameters
        parameters = csv_reader.next()
        name = parameters[0]
        rgbList = [256*256*int(parameters[1])+256*int(parameters[2])+int(parameters[3])]
        timeList = [float(parameters[5])]

        #while CSV file not empty
        while True:
             
             try:
                  parameters = csv_reader.next()
             except:
                  break

             #if LED Group different than last row
             if (name != parameters[0]):
                   #send current fadeListRGB parameters to Nao
                   self.nao.ledProxy.post.fadeListRGB(name, rgbList, timeList)
                   #print 'ledProxy.post.fadeListRGB(', name, rgbList, timeList, ')'
                   #intialize fadeListRGB parameters
                   name = parameters[0]
                   rgbList = []
                   timeList = []

             #add this row to fadeListRGB parameters
             rgbList.append(256*256*int(parameters[1])+256*int(parameters[2])+int(parameters[3]))
             timeList.append(float(parameters[5]))

        #all done - send current fadeListRGB parameters to Nao
        self.nao.ledProxy.post.fadeListRGB(name, rgbList, timeList) 
        #print 'ledProxy.post.fadeListRGB(', name, rgbList, timeList, ')'
              
        return file_load

    def GetAvailableModules(self):
        
        the_dir, list_dir=FindPath("modules")
        
        dir_file = []
        for directory in list_dir:
            if not directory.startswith('.'):
                list_subdir = os.listdir(the_dir+"/"+directory)
                module_files = [directory+"/"]
                for file_name in list_subdir:
                    if not file_name.startswith("."):
                        module_files.append(file_name)
                        #module_files.append([directory,file_name])
                dir_file.append(module_files)
        return dir_file

    ###############################################################################
    ## This function returns the available gestures located in the gesture dir.
    ###############################################################################
    def GetAvailableGestures(self):
        """Returns available gestures in a list"""
        the_dir, list_gestures=FindPath("gestures")
##        mylist = []     
##        for x in list_gestures:
##            if x.endswith(".py") or x.endswith(".ges"):
##                mylist.append(x)
##          
##        return list_gestures
        return FindExt(list_gestures, [".py", ".ges"])
    
    ###############################################################################
    ## This function returns the available gestures located in the gesture dir.
    ###############################################################################
    def GetAvailableLEDPatterns(self):
        """Returns available gestures in a list"""
        the_dir, list_led = FindPath("led")
##        mylist=[]
##        for x in list_led:
##            if x.endswith(".csv") or x.endswith(".led"):
##                mylist.append(x)
##                
##        return mylist
        return FindExt(list_led, [".csv", ".led"])

    ###############################################################################
    ## This function returns the available dialogs located in the dialogs dir.
    ###############################################################################
    def GetAvailableDialogs(self):
        """Returns available dialogs in a list"""
##        list_path = sys.path
##        found = []
##        for i in range (0,len(list_path)):
##            if os.path.exists(list_path[i]+"/dialogs"):
##                found.append(i)
##            
##        if found == []:
##            print "Could not find /dialogs directory!"
##            raise IOError
##            return None
##
##        list_dlg=[]
##        mylist = []
##        for fi in found:
##            temp=os.listdir(list_path[fi]+"/dialogs")
##            list_dlg=list_dlg + temp
##
##            ## collect non csv/dlg files
##            for x in list_dlg:
##                if x.endswith(".csv") or x.endswith(".dlg"):
##                    mylist.append(x)
##
##        return mylist
        the_dir, list_dlg =  FindPath("dialogs")
        return FindExt(list_dlg, [".csv",".dlg"])
    #########################################################################
    ## Loads a dialog csv file and converts its logic and questions/messages
    ## to dictionaires for use in a smach state machine
    #########################################################################
    def LoadDialog(self, file_name):
        """ Give the filename of the dialog in the /dialogs folder. Extension should be .csv or .dlg."""
        list_path = sys.path
        filefound=False
        for i in range (0,len(list_path)):
            if os.path.exists(list_path[i]+"/dialogs/"+file_name):
                filefound=True
                break

        if not filefound:
            print "Dialog file "+str(file_name)+" not found in PYTHONPATH"
            return

        file_load = open(list_path[i]+"/dialogs/"+file_name)

        #read all rows of CSV file (assumes delimiter is ';')
        csv_reader = csv.reader(file_load, delimiter=';')

        return csv_reader


if __name__ == "__main__":
    global ni
    ni=n.Nao_Interface("ni","127.0.0.1")
    script=Nao_Script(ni)
    print script.GetAvailableModules(), "\n"
    l=script.GetAvailableGestures()
    print l, "\n"
    print script.GetAvailableLEDPatterns(), "\n"
    print script.GetAvailableDialogs(), "\n"
 
    s=raw_input("Show available gestures? ")
    if s=="yes":
        for i in l:
            print i
            ni.Say(i.split(".")[0])
            script.RunMovement(i, False)
