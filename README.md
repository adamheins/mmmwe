# Minimal Mobile Manipulator Waiter Example

This repo provides a minimal PyBullet simulation example of the mobile
manipulator waiter robot (used in [this
project](https://github.com/utiasDSL/upright)).

## Installation and setup

This repo can be used as a ROS package but does not need to be run in a catkin
workspace. Clone into some location:
```
git clone https://github.com/adamheins/mmmwe.git ~
```
You'll need to clone the
[universal_robot](https://github.com/ros-industrial/universal_robot) repo into
the same place, because the URDF file for the UR10 arm depends on it:
```
git clone https://github.com/ros-industrial/universal_robot.git ~
```

Now head into the directory and install Python dependencies:
```
cd ~/mmmwe
pip install -r requirements.txt
```

## Usage

A simple example script is provided in `example.py`, which loads the robot and
executes a simple inverse kinematics control loop to reach a desired position
with the end effector.
