#!/usr/bin/env python

# This node will navigate the AR Drone 2.0 to the OptiTrack reference point
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy

# Importing messages
from visualization_msgs.msg import Marker 	# for receiving marker detection


class OptiTrackController():
    def __init__(self, controller):

        self.controller = controller
        self.landing = False

        # If marker is detected it calls the detected(data) function
        # rospy.Subscriber("/drone", Marker, self.flying)

        # If marker is detected it calls the setLanding(data) function
        rospy.Subscriber("/visualization_marker", Marker, self.setLanding)

    def flying(self, data):
        if not self.landing:
            rospy.loginfo("Flying")

            # Here comes the positioning
            self.controller.SetCommand(0, 0, 0, 0)

    def setLanding(self, data):
        self.landing = True
