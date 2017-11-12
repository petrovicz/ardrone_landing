#!/usr/bin/env python

# This node will land the AR Drone 2.0 in case of marker detection
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy


class OptiTrackController():
    def __init__(self):
        self.status = -1
        rospy.loginfo("Initiating OptiTrackController")

        # If marker is detected it calls the detected(data) function
        # rospy.Subscriber("/optitrack_message", Marker, self.flying)

    def flying(self, data):
        rospy.loginfo("Flying")
