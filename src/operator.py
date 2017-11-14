#!/usr/bin/env python

# This node will control the whole scenario
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

import roslib; roslib.load_manifest('ardrone_tutorials')
from drone_controller import BasicDroneController

from std_srvs.srv import Empty

import landing
import optitrack
import rospy
import time


def toggleCam():
    rospy.wait_for_service('/ardrone/togglecam')
    togglecam = rospy.ServiceProxy('/ardrone/togglecam', Empty)

    try:
        togglecam()
    except rospy.ServiceException, e:
        print "Service did not process request: %s" % str(e)


if __name__ == '__main__':
    try:
        # Configuration
        rospy.init_node('operator')
        rospy.loginfo("Starting operator")
        time.sleep(1)
        controller = BasicDroneController()

        toggleCam()

        rospy.loginfo("Taking off drone")
        # controller.SendTakeOff()
        time.sleep(1)

        rospy.loginfo("Starting OptiTrackController")
        OptiTrackController = optitrack.OptiTrackController(controller)
        rospy.loginfo("Starting LandingController")
        landingController = landing.LandingController(controller)

        while not rospy.is_shutdown():
            # controller.sendCommand()
            time.sleep(1)

    except rospy.ROSInterruptException:
        pass
