# -*- encoding: UTF-8 -*-

''' A script for testing diverse things .... '''

import argparse
import motion
import naoqi
from naoqi import ALProxy

NAO_IP_WIRED = "169.254.129.144"
NAO_IP_LABNET = "172.17.117.239"
NAO_IP_HUB = "192.168.0.1"
NAO_DEF_PORT = 9559

def main(robotIP, PORT=NAO_DEF_PORT) :
    
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    tts.say("Hello ! I feel good today !")





if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=NAO_IP_LABNET,
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=NAO_DEF_PORT,
                        help="Robot port number")
    args = parser.parse_args()

    main(args.ip, args.port)




