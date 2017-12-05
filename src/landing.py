#!/usr/bin/env python

# This node will land the AR Drone 2.0 in case of marker detection
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

import roslib; roslib.load_manifest('ardrone_autonomy')

# Importing libraries
import rospy
import time
import globalvars

# Importing messages and services
from visualization_msgs.msg import Marker
from sensor_msgs.msg import CameraInfo
from std_srvs.srv import Empty


class LandingController():
    def __init__(self, controller):

        self.controller = controller
        self.performed = False

        # If marker is detected it calls the performLanding(data) function
        rospy.Subscriber("/visualization_marker", Marker, self.perfromAction)

        self.camera = rospy.Subscriber("/ardrone/camera_info",
                                       CameraInfo, self.toggleCam)

    def perfromAction(self, data):

        if globalvars.detected and not self.performed:

            if data.id == 0:
                self.action0()

            if data.id == 1:
                self.action1()

    def toggleCam(self, data):
        # Toggle cam if not set correctly
        if (
            data.header.frame_id == "ardrone_base_frontcam" and
            rospy.get_param(
                "/ar_track_alvar/output_frame") == "/ardrone_base_bottomcam" or
            data.header.frame_id == "ardrone_base_bottomcam" and
            rospy.get_param(
                "/ar_track_alvar/output_frame") == "/ardrone_base_frontcam"
        ):
            rospy.wait_for_service('/ardrone/togglecam')
            togglecam = rospy.ServiceProxy('/ardrone/togglecam', Empty)

            try:
                togglecam()
            except rospy.ServiceException, e:
                print "Service did not process request: %s" % str(e)

        self.camera.unregister()

    def action0(self):
        self.performed = True
        rospy.loginfo("Action: 0")

        self.controller.SetCommand(0, 0, 0, 1)
        time.sleep(7)

        self.controller.SetCommand(0, 0.2, 0, 0)
        time.sleep(4)

        self.controller.SetCommand(0, -1, 0, -1)

        self.controller.SendLand()

    def action1(self):
        self.performed = True
        rospy.loginfo("Action: 1")

        self.controller.SetCommand(0.1, 0, 0, -1)
        time.sleep(3)

        self.controller.SetCommand(0, 0.2, 0, -1)
        time.sleep(3)

        self.controller.SetCommand(0, -1, 0, -1)
        time.sleep(1)

        self.controller.SetCommand(-0.1, 0, 0, -1)
        time.sleep(3)

        self.controller.SendLand()
