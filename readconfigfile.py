import os

search_paths = [os.getcwd()]

#environment=os.getenv('PATH').split(os.pathsep)
#search_paths.append(environment)

def ReadConfigKey(key, configfile='nao.cfg'):
    for thepath in search_paths:
            if thepath[-1]!=os.sep:
                thepath+=os.sep
            if configfile[0]==os.sep: #prevent searching in root unless root is in the search_paths
                configfile=configfile[1:]
            if os.path.exists(thepath+configfile):
                    #print 'Reading: ' + thepath+configfile
                    theFile=open(thepath+configfile)
                    theContent=theFile.readlines()
                    for theline in theContent:
                            if theline.strip().startswith(key):
                                    keyvalue=theline.strip().split('=')
                                    return keyvalue
                    break

def ReadConfigFile(configfile='nao.cfg'):

    keydict={}
    for thepath in search_paths:
            if thepath[-1]!=os.sep:
                thepath+=os.sep
            if configfile[0]==os.sep: #prevent searching in root unless root is in the search_paths
                configfile=configfile[1:]
            if os.path.exists(thepath+configfile):
                    #print 'Reading: ' + thepath+configfile
                    theFile=open(thepath+configfile)
                    theContent=theFile.readlines()
                    for theline in theContent:
                            if not theline.find('=')<0 and not theline.strip().startswith('#'):
                                    keyvalue=theline.strip().split('=')
                                    keydict[keyvalue[0]]=keyvalue[1]
            break
    return keydict

if __name__ == "__main__":

    mykey='IP_NAO'
    mykeyvalue = ReadConfigKey(mykey)
    print 'The value of %s is: %s\n'%(mykeyvalue[0], mykeyvalue[1])

    mydict=ReadConfigFile()
    for akey in mydict:
        print 'The value of %s is: %s'% (akey,mydict[akey])
