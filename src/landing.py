#!/usr/bin/env python

# This node will land the AR Drone 2.0 in case of marker detection
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy

# Importing messages and services
from visualization_msgs.msg import Marker
from sensor_msgs.msg import CameraInfo
from std_srvs.srv import Empty


class LandingController():
    def __init__(self, controller):

        self.controller = controller

        # If marker is detected it calls the performLanding(data) function
        rospy.Subscriber("/visualization_marker", Marker, self.perfromLanding)

        self.camera = rospy.Subscriber("/ardrone/camera_info",
                                       CameraInfo, self.toggleCam)

    def perfromLanding(self, data):
        rospy.loginfo("x:" + str(data.pose.position.x))
        rospy.loginfo("y:" + str(data.pose.position.y))
        rospy.loginfo("z:" + str(data.pose.position.z))

        # Here comes the positioning
        self.controller.SetCommand(0, 0, 0, 0)

    def toggleCam(self, data):
        # Toggle to bottomcam if not in use
        if data.header.frame_id == "ardrone_base_bottomcam":
            self.camera.unregister()
        else:
            rospy.wait_for_service('/ardrone/togglecam')
            togglecam = rospy.ServiceProxy('/ardrone/togglecam', Empty)

            try:
                togglecam()
            except rospy.ServiceException, e:
                print "Service did not process request: %s" % str(e)
