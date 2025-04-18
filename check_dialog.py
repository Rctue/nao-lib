# -*- coding: utf-8 -*-
from naoqi import ALProxy

"""Events

Event: "Dialog/Answered"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised each time the robot answers. Contains the last answer. Subscribing to this event starts ALDialog.

Example

u:(what did you say before) I said $Dialog/Answered
Event: "Dialog/LastInput"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised each time the robot catches a human input. Contains the last human input.

Example

u:(hello) $Dialog/LastInput
Event: "Dialog/LastAnswer"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Contains the last robot’s answer that is not coming from a rule u:(e:NotUnderstood)

Event: "Dialog/SaidMisunderstood"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised when the robot didn’t understand. Equivalent to Dialog/NotUnderstood().

Event: "Dialog/NotUnderstoodEvent"
callback(std::string eventName, std::string subscriberIdentifier)
Raised when the robot didn’t understand and there is a e:Dialog/NotUnderstood matched in the topic.

Event: "Dialog/Tag"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised when the robot says a sentence with a tag inside. The event’s value is the tag’s name.

Event: "Dialog/Focus"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised when the dialog engine changes the currently focused topic. The new focused topic’s name is in the event’s value.

Event: "Dialog/FocusDescription"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised when the dialog engine changes the currently focused topic. The event’s value is the topic’s description. The value is empty if the topic does not have any description.

Event: "Dialog/ActivateTopic"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised when the dialog engine activates a topic. The topic’s name is the event’s value.

Event: "Dialog/DeactivateTopic"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Raised when the dialog engine deactivates a topic. The topic’s name is the event’s value.

Event: "Dialog/OpenSession"
callback(std::string eventName, int id, std::string subscriberIdentifier)
Raised when the dialog engine has finished opening a session. Value is the session ID.

Event: "Dialog/IsStarted"
callback(std::string eventName, int state, std::string subscriberIdentifier)
Raised when the dialog engine starts or stops. The value is “1” for start, “0” for stop.

Event: "Dialog/NothingToSay"
callback(std::string eventName, std::string subscriberIdentifier)
Raised when ^gotoRandom didn’t find any proposal to say.

Event: "Dialog/CannotMakeIt"
callback(std::string eventName, std::string behaviorName, std::string subscriberIdentifier)
Internal event. Do not use.

Event: "Dialog/Language/English"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Value = 1 if the given language (here it’s English) is installed. The variable is not created if the language is not installed.

Event: "Dialog/Language/French"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Value = 1 if the given language (here it’s French) is installed. The variable is not created if the language is not installed.

Data

Event: "Dialog/MatchedApp"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
When Dialog/LastAnswer is raised, Dialog/MatchedApp contains the application that matched.

Event: "Dialog/MatchedInput"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
When Dialog/LastAnswer is raised, Dialog/MatchedInput contains the current human input in the rule that matched.

Event: "Dialog/MatchedTopic"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
When Dialog/LastAnswer is raised, Dialog/MatchedTopic contains the topic that matched.

Event: "Dialog/RobotModel"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Data that contains “juliette” on Pepper robot and “nao” on nao robot.

Event: "Dialog/RobotName"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Data that contains “pepper” or “nao” depending robot model.

Event: "Dialog/MatchedLine"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
When Dialog/LastAnswer is raised, Dialog/MatchedLine contains the line in the topic that matched.

Event: "Dialog/TalkTime"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Current talk time in seconds since last ALDialog::openSession and last human sentence. Dialog/TalkTime is not updated on forceInput API call.

Event: "Dialog/DateCode"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Concatenation: month number + day number. Ex: 1225 for Christmas.

Event: "Dialog/Default"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Value = 1 if the current time is between 11 AM and 7 PM.

Event: "Dialog/Morning"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Value = 1 if the current time is between 5 AM and 11 AM.

Event: "Dialog/Night"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Value = 1 if current time is between 7 PM and 5 AM.

Event: "Dialog/Year"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Current year (format: YYYY).

Event: "Dialog/Hour"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Current hour (in 24-hour format).

Event: "Dialog/Minute"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Current minute.

Event: "Dialog/Second"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Current second.

Event: "Dialog/CurrentString"
callback(std::string eventName, std::string value, std::string subscriberIdentifier)
Currently processed human input.Events

"""

IP='192.168.0.112'
PORT = 9559 #look up in choregraphe in the Edit/Preferences menu on the "Virtual robot" tab for the PORT settings for simulated robot

memproxy = ALProxy('ALMemory', IP, PORT)

def print_dialog_data():
    print "------------ Dialog Data --------------------"
    print "is started: " + memproxy.getData('Dialog/IsStarted')
    print "last answered output: " + memproxy.getData('Dialog/Answered')
    print "last input: " + memproxy.getData('Dialog/LastInput')
##    print "last misunderstood input: " + memproxy.getData('Dialog/SaidMisunderstood') # apparently not available in older versions of naoqi (2.1?)
    print "focus: " + memproxy.getData('Dialog/Focus')
    print "tag: " + memproxy.getData('Dialog/Tag')
    print "activate topic: " + str(memproxy.getData('Dialog/ActivateTopic'))
    print "deactivate topic: "+ str(memproxy.getData('Dialog/DeactivateTopic'))
    print "last matched topic: " + memproxy.getData('Dialog/MatchedTopic')
    print "last matched input: " + memproxy.getData('Dialog/MatchedInput')
    print "last matched line: " + memproxy.getData('Dialog/MatchedLine')
    print "current string: " + memproxy.getData('Dialog/CurrentString')
    print "variable $sea_food: " + memproxy.getData('sea_food') # variables created in the Dialog ($sea_food) are directly accessible via ALMemory 
    

done = False
while not done:

    # Option 1: use a blocking call that waits for a data change to control the flow
    print_dialog_data()
    last_input = memproxy.getDataOnChange('Dialog/LastInput',0) # this is a blocking call that waits for a change

    # Option 2: alternatively use the non-blocking call last_input = memproxy.getData('Dialog/LastInput')
    #           and then clear the contents using memproxy.insertData('Dialog/LastInput','').
    #           This prevents that the Last Input triggers the same response multiple times.
##    last_input= memproxy.getData('Dialog/LastInput')
##    if last_input!='':
##        print_dialog_data()
##        memproxy.insertData('Dialog/LastInput','')

    if last_input=='quit':
        done = True
    
