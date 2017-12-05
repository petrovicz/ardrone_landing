#!/usr/bin/env python

# This node will navigate the AR drone 2.0 to the OptiTrack reference point
# https://uavlab.itk.ppke.hu
# Author : Benedek Petrovicz

# Importing libraries
import rospy
import time
import globalvars

# Importing messages
from visualization_msgs.msg import Marker 	# for receiving marker detection
from geometry_msgs.msg import PoseStamped


class OptiTrackController():
    def __init__(self, controller):

        self.controller = controller
        self.arrived = False
        self.destination = PoseStamped
        self.forward = 0
        self.right = 0
        self.speed = 0.1

        rospy.Subscriber('/vrpn_client_node/ardrone/pose',
                         PoseStamped, self.transform)

        rospy.Subscriber('/vrpn_client_node/destination/pose',
                         PoseStamped, self.setDestination)

        # If marker is detected it calls the detected(data) function
        rospy.Subscriber("/ardrone/pose", PoseStamped, self.flying)

        # If marker is detected it calls the setLanding(data) function
        rospy.Subscriber("/visualization_marker", Marker, self.setDetected)

        self.publisher = rospy.Publisher('/ardrone/pose',
                                         PoseStamped, queue_size=10)

    def flying(self, data):

        roll = 0
        pitch = 0
        z_velocity = 0

        if not self.arrived:

            destination = self.destination.pose.position
            drone = data.pose.position
            treshold = 0.3

            if (
                -treshold < (destination.x - drone.x) < treshold and
                -treshold < (destination.y - drone.y) < treshold and
                self.forward == 0 and self.right == 0
            ):
                time.sleep(1)
                self.arrived = True

            rospy.loginfo("-------------")

            if drone.x < (destination.x - treshold):
                rospy.loginfo("Going Backward")
                self.forward = -1
                pitch = -self.speed * 2

            if drone.x > (destination.x + treshold):
                rospy.loginfo("Going Forward")
                self.forward = 1
                pitch = self.speed / 15

            if drone.y < (destination.y - treshold):
                rospy.loginfo("Going Right")
                self.right = 1
                roll = -self.speed

            if drone.y > (destination.y + treshold):
                rospy.loginfo("Going Left")
                self.right = -1
                roll = self.speed

            # Countering previous velocities
            if -treshold < (destination.x - drone.x) < treshold:
                if self.forward == 1:
                    pitch = -self.speed * 3
                if self.forward == -1:
                    pitch = self.speed
                self.forward = 0

            if -treshold < (destination.y - drone.y) < treshold:
                if self.right == 1:
                    roll = self.speed * 2
                if self.right == -1:
                    roll = -self.speed * 2
                self.right = 0

        elif not globalvars.detected:
            z_velocity = -1

        # Finaly, set velocities
        if not globalvars.detected:
            self.controller.SetCommand(roll, pitch, 0, z_velocity)

    def setDetected(self, data):
        if self.arrived:
            globalvars.detected = True

    def setDestination(self, data):
        data.pose.position.y, data.pose.position.z = data.pose.position.z, data.pose.position.y
        data.pose.position.x, data.pose.position.y = data.pose.position.y, data.pose.position.x
        self.destination = data

    def transform(self, data):
        data.pose.position.y, data.pose.position.z = data.pose.position.z, data.pose.position.y
        data.pose.position.x, data.pose.position.y = data.pose.position.y, data.pose.position.x
        self.publisher.publish(data)
