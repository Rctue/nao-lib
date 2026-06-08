import qi
import argparse
import sys

### usage: python stopLoadedTopics.py --ip $YOUR_ROBOTS_IP_ADDRESS --port $YOUR_ROBOT_PORT

def main(session):
	ALDialog = session.service("ALDialog")
	loadedTopicsEnglish = ALDialog.getLoadedTopics("English")
	print("Loaded topics:", ALDialog.getAllLoadedTopics())
	
	for x in loadedTopicsEnglish:
		print("Do you want to unload topic: ", x)
		confirmationInput = input("(y/n)")
		if (confirmationInput == "y"):
			ALDialog.unloadTopic(x)
			print("Topic unloaded")
		elif (confirmationInput == "n"):
			print("Topic is not unloaded")
		else:
			print("no valid input, topic is not unloaded, going to next topic")
			
	print("Done, loaded topics left: ", ALDialog.getAllLoadedTopics())
	print("If you want to remove more topics, re-run this script again")
	quit()
		
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot's IP address. If on a robot or a local Naoqi - use '127.0.0.1' (this is the default value).")
    parser.add_argument("--port", type=int, default=9559,
                        help="port number, the default value is OK in most cases")

    args = parser.parse_args()
    session = qi.Session()
    try:
        session.connect("tcp://{}:{}".format(args.ip, args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at IP {} (port {}).\nPlease check your script's arguments."
               " Run with -h option for help.".format(args.ip, args.port))
        sys.exit(1)
    main(session)
