#!/usr/bin/env python

# This node will navigate the AR Drone 2.0 to the OptiTrack reference point
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy


class OptiTrackController():
    def __init__(self, controller):

        self.controller = controller

        # If marker is detected it calls the detected(data) function
        # rospy.Subscriber("/optitrack_message", Marker, self.flying)

    def flying(self, data):
        rospy.loginfo("Flying")

        # Here comes the positioning
        self.controller.SetCommand(0, 0, 0, 0)
