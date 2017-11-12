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
        rospy.init_node('operator')
        rospy.loginfo("Starting operator")
        time.sleep(1)
        controller = BasicDroneController()

        # TODO: call rosservice /ardrone/togglecam

        rospy.loginfo("Taking off drone")
        # controller.SendTakeOff()
        time.sleep(1)

        rospy.loginfo("Starting OptiTrackController")
        OptiTrackController = optitrack.OptiTrackController()
        rospy.loginfo("Starting LandingController")
        landingController = landing.LandingController()

        while not rospy.is_shutdown():
            time.sleep(1)

    except rospy.ROSInterruptException:
        pass
