################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################
import sys
import os


import numpy as np
import pylab as pl
import glob
import cv2
import subprocess
import math
import re
import pickle

#currentPath = os.path.dirname(os.path.abspath(__file__))
#sys.path.insert(0, currentPath + "/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib")
sys.path.append("../Leapmotion-GesturePredicted/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib")
# print currentPath + "/LeapDeveloperKit_2.3.1+31549_mac/LeapSDK/lib"
import Leap, sys, thread, time
from Leap import CircleGesture, KeyTapGesture, ScreenTapGesture, SwipeGesture

class SampleListener(Leap.Listener):
    finger_names = ['Thumb', 'Index', 'Middle', 'Ring', 'Pinky']
    bone_names = ['Metacarpal', 'Proximal', 'Intermediate', 'Distal']
    state_names = ['STATE_INVALID', 'STATE_START', 'STATE_UPDATE', 'STATE_END']
    predict_buf = []
    answer=0 

    def on_init(self, controller):
        print "Initialized"
        print ""

    def on_connect(self, controller):
        #print "Connected"
        # Enable gestures
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE);
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP);
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE);

    def on_disconnect(self, controller):
        # Note: not dispatched when running in a debugger.
        #print "Disconnected"
        print ""
    def on_exit(self, controller):
        #print "Exited"
        print ""

    def on_frame(self, controller):
        # Get the most recent frame and report some basic information
        frame = controller.frame()
        # Get hands
        for hand in frame.hands:

            handType = "Left hand" if hand.is_left else "Right hand"
            # Get the hand's normal vector and direction
            normal = hand.palm_normal
            direction = hand.direction

            # Calculate the hand's pitch, roll, and yaw angles
	    palm=hand.palm_position
	    width = hand.palm_width
            #print "width: %s "%(width)

	    thumb = hand.fingers.finger_type(Leap.Finger.TYPE_THUMB)[0].tip_position
	    index = hand.fingers.finger_type(Leap.Finger.TYPE_INDEX)[0].tip_position

	    thumb_length=(thumb-palm).magnitude/width
	    index_length=(index-palm).magnitude/width

            # print "thumb: %s ,lenghth: %s"%(
            # thumb, thumb_length)
            # print "index: %s ,lenghth: %s"%(
            # index, index_length)
	    
            if thumb_length>0.8:
	        self.answer=3
	    elif index_length<0.7:
                self.answer=2
	    else: 
                self.answer=1 
	    # print self.answer
        if (frame.hands.is_empty and frame.gestures().is_empty):
            self.answer=0
            #print "No hand~~~~~~~~"
    def on_focus_lost(self, controller):
        print "Unfocused"


    def state_string(self, state):
        if state == Leap.Gesture.STATE_START:
            return "STATE_START"

        if state == Leap.Gesture.STATE_UPDATE:
            return "STATE_UPDATE"

        if state == Leap.Gesture.STATE_STOP:
            return "STATE_STOP"

        if state == Leap.Gesture.STATE_INVALID:
            return "STATE_INVALID"

def predictgesture():
    # Keep this process runniing until Enter is pressed
    #print "Press Enter to quit..."
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)

def predict():
    global listener
    # Create a sample listener and controller
    listener = SampleListener()
    global controller
    controller = Leap.Controller()
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    thread.start_new_thread(predictgesture,())

def getAnswer():
    global listener
    return listener.answer
"""
if __name__ == "__main__":
    global listener
    listener = SampleListener()
    controller = Leap.Controller()
    # Have the sample listener receive events from the controller
    controller.add_listener(listener)
    try:
        sys.stdin.readline()
    except KeyboardInterrupt:
        pass
    finally:
        # Remove the sample listener when done
        controller.remove_listener(listener)
"""
