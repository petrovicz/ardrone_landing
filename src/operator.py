#!/usr/bin/env python

# This node will control the whole scenario
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

import roslib; roslib.load_manifest('ardrone_tutorials')
from drone_controller import BasicDroneController

import landing
import optitrack
import rospy
import time


if __name__ == '__main__':
    try:
        # Configuration
        rospy.init_node('ardrone_landing')
        controller = BasicDroneController()

        # This sleep ensures that we can already publish,
        # because in ardrone_tutorials the 'latched' option is not enabled
        time.sleep(2)

        rospy.loginfo("Taking off drone")
        controller.SendTakeoff()

        # Hovering state in ardrone_autonomy is imperfect so wait until
        # the drone goes idle
        time.sleep(2)

        rospy.loginfo("Starting OptiTrackController")
        OptiTrackController = optitrack.OptiTrackController(controller)
        rospy.loginfo("Starting LandingController")
        landingController = landing.LandingController(controller)

        rospy.spin()

    except rospy.ROSInterruptException:
        pass
