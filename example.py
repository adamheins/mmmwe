#!/usr/bin/env python3
import numpy as np
import pybullet as pyb
import pybullet_data
import pyb_utils
import xacrodoc


DURATION = 10  # seconds
STEPS_PER_SEC = 1000
SIM_STEPS = DURATION * STEPS_PER_SEC
SIM_TIMESTEP = 1.0 / STEPS_PER_SEC
GRAVITY = np.array([0, 0, -9.81])

ROBOT_HOME = np.array([0, 0, 0, 1.5708, -0.7854, 1.5708, -0.7854, 1.5708, 1.3100])


def main():
    # needed to find the ur_description package
    xacrodoc.packages.look_in([".."])
    includes = [
        "$(find mmmwe)/assets/mm.urdf.xacro",
        "$(find mmmwe)/assets/tray.urdf.xacro",
    ]
    doc = xacrodoc.XacroDoc.from_includes(includes)

    pyb.connect(pyb.GUI)
    pyb.setTimeStep(SIM_TIMESTEP)
    pyb.setGravity(*GRAVITY)

    # ground plane
    pyb.setAdditionalSearchPath(pybullet_data.getDataPath())
    pyb.loadURDF("plane.urdf", [0, 0, 0], useFixedBase=True)

    # robot
    with doc.temp_urdf_file_path() as urdf_path:
        robot_id = pyb.loadURDF(urdf_path, [0, 0, 0], useFixedBase=True)
    robot = pyb_utils.Robot(robot_id)
    robot.reset_joint_configuration(ROBOT_HOME)

    r0 = robot.get_link_frame_pose()[0]
    goal = r0 + np.array([1, 1, -0.5])

    for i in range(SIM_STEPS):
        # get robot feedback in joint space
        # q, v = robot.get_joint_states()

        # simple inverse kinematics controller
        r = robot.get_link_frame_pose()[0]
        J = robot.compute_link_frame_jacobian()[:3, :]
        u = np.linalg.lstsq(J, goal - r, rcond=None)[0]
        robot.command_velocity(u)

        pyb.stepSimulation()


main()
