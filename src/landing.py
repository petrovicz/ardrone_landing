#!/usr/bin/env python

# This node will land the AR Drone 2.0 in case of marker detection
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy

# Importing messages
from visualization_msgs.msg import Marker 	# for receiving marker detection


class LandingController():
    def __init__(self):
        self.status = -1
        rospy.loginfo("Initiating LandingController")

        # If marker is detected it calls the detected(data) function
        rospy.Subscriber("/visualization_marker", Marker, self.detected)

    def land():
        rospy.loginfo("Landing")

    def detected(self, data):
        rospy.loginfo("Detected")
