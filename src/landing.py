#!/usr/bin/env python

# This node will land the AR Drone 2.0 in case of marker detection
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing control functions from ardrone_tutorials
import roslib; roslib.load_manifest('ardrone_tutorials')
from drone_controller import BasicDroneController

# Importing libraries
import rospy
import time

# Importing messages
from visualization_msgs.msg import Marker 	# for receiving marker detection


def detected(data):
    rospy.loginfo("Marker detected")
    return


def flying():
    while not rospy.is_shutdown():
        time.sleep(1)


if __name__ == '__main__':
    try:
        # Configuration
        rospy.init_node('landing')
        controller = BasicDroneController()

        # If marker is detected it calls the detected(data) function
        rospy.Subscriber("/visualization_marker", Marker, detected)

        flying()
    except rospy.ROSInterruptException:
        pass
