# -*- encoding: UTF-8 -*-

''' A script for testing diverse things .... '''

import argparse
import sys
import time

import motion
import naoqi
import almath
from naoqi import ALProxy
from naoqi import ALBroker
from naoqi import ALModule

NAO_IP_WIRED = "169.254.129.144"
NAO_IP_LABNET = "172.17.117.239"
NAO_IP_HUB = "192.168.0.1"
NAO_DEF_PORT = 9559

def main(robotIP, PORT=NAO_DEF_PORT) :
    
    proxTTS = ALProxy("ALTextToSpeech", robotIP, PORT)
    proxMotion = ALProxy("ALMotion", robotIP, PORT)
    proxPosture = ALProxy("ALRobotPosture", robotIP, PORT)

    proxMotion.wakeUp()
    

    proxMotion.rest()




if __name__ == "__main__" :
    
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default=NAO_IP_LABNET,
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=NAO_DEF_PORT,
                        help="Robot port number")
    args = parser.parse_args()

    main(args.ip, args.port)




