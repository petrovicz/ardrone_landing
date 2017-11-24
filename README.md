# ardrone_landing [![kinetic](https://img.shields.io/badge/ros-kinetic-blue.svg)](http://wiki.ros.org/kinetic)
Performs autonomus landing of an AR Drone 2.0 with the help of marker detection and OptiTrack positioning
> Note: This package is only the frame of the project yet. Future commits will make it work.

## Prerequisites:
1. AR Drone 2.0
2. OptiTrack camera system
3. Install ardrone_autonomy
4. Install ros kinetic
5. Install ardrone_tutorials
6. Install ar_track_alvar
7. Install vrpn_client_ros

## How to use
1. Launch **autonomus_landing** for starting the **ardrone_driver** and **ar_track_alvar**  
```bash
roslaunch ardrone_landing autonomus_landing.launch
```
2. Ensure that the status of the drone is **not** set to **Emergency**. You can toggle it with the following command  
```bash
rostopic pub /ardrone/reset std_msgs/Empty -1
```
3. Run the **operator**  
```bash
rosrun ardrone_landing operator.py
```
