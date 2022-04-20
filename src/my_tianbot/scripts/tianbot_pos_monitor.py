#!/usr/bin/env python

import rospy
import numpy as np
import matplotlib.pyplot as plt
from nav_msgs.msg import Odometry, Path

from turtlesim.msg import Pose

x, y = [], []

def callback(data):
    xx = data.pose.pose.position.x
    yy = data.pose.pose.position.y
    # xx = data.x
    # yy = data.y

    x.append(xx)
    y.append(yy)

def monitor():
    rospy.init_node('pos_monitor', anonymous=True)
    rospy.Subscriber('tianbot_mini/odom', Odometry, callback)
    # rospy.Subscriber('turtle1/pose', Pose, callback)

    rospy.spin()

if __name__ == '__main__':
    monitor()
    plt.plot(x, y)
    plt.show()