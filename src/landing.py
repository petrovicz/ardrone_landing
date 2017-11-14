#!/usr/bin/env python

# This node will land the AR Drone 2.0 in case of marker detection
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy

# Importing messages
from visualization_msgs.msg import Marker 	# for receiving marker detection


class LandingController():
    def __init__(self, controller):

        self.controller = controller

        # If marker is detected it calls the performLanding(data) function
        rospy.Subscriber("/visualization_marker", Marker, self.perfromLanding)

    def perfromLanding(self, data):
        rospy.loginfo("x:" + str(data.pose.position.x))
        rospy.loginfo("y:" + str(data.pose.position.y))
        rospy.loginfo("z:" + str(data.pose.position.z))

        # Here comes the positioning
        self.controller.SetCommand(0, 0, 0, 0)
