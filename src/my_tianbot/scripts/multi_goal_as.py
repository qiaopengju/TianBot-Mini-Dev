#!/usr/bin/env python
# control the linear speed and angular speed of the bot

import rospy
import actionlib
from actionlib_msgs.msg import *
from geometry_msgs.msg import PoseStamped, Point, Pose, Quaternion, Twist
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from tf.transformations import quaternion_from_euler
from visualization_msgs.msg import Marker
from math import radians, pi
import numpy as np

class MultiMoveBase():
    def __init__(self):
        rospy.init_node('goal_as', anonymous=True)

        goal_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
        marker_pub = rospy.Publisher('waypoint_markers', Marker, queue_size=10)
        rate = rospy.Rate(10) # 10hz

        while not rospy.is_shutdown():
            waypoints = []
            self.init_markers() # Initialize the markers for RViz

            # # Input
            while True:
                goal_num = input('The total number of goal point : ')
                if type(goal_num) == int and goal_num > 0: break
                else:
                    print('Point number must be an integer greater than 0 , input again!\n')
            for i in range(goal_num):
                while True:
                    xx = input('Goal Pos X_%d: ' %(i+1))
                    if type(xx) == float or type(xx) == int: break
                    else:
                        print('Position.x must be float, input again!\n')
                while True:
                    yy = input('Goal Pos Y_%d: ' %(i+1))
                    if type(yy) == float or type(yy) == int: break
                    else:
                        print('Position.y must be float, input again!\n')
                # Append goal point to list
                goal_tmp = Pose()
                goal_tmp.position.x = xx
                goal_tmp.position.y = yy
                # goal_tmp.orientation = quaternion_from_euler(0, 0, 90)
                goal_tmp.orientation.w = 1.0
                self.marker.points.append(goal_tmp.position)
                waypoints.append(goal_tmp)

                # Move base action server
                self.cmd_vel_pub = rospy.Publisher("tianbot_mini/cmd_vel", Twist, queue_size=10)
                self.move_base = actionlib.SimpleActionClient("move_base", MoveBaseAction)
    
            for i in range(goal_num):
                marker_pub.publish(self.marker)

                goal = MoveBaseGoal()
                goal.target_pose.header.frame_id = 'map'
                goal.target_pose.header.stamp = rospy.Time.now()
                goal.target_pose.pose = waypoints[i]

                # get orientation quaternions
                g2g_x = waypoints[(i+1)%goal_num].position.x - waypoints[i].position.x
                g2g_y = waypoints[(i+1)%goal_num].position.y - waypoints[i].position.y
                len = np.sqrt(g2g_x**2 + g2g_y**2)
                if len == 0: eular_angle = 0
                else: eular_angle = np.arccos(g2g_x / len)
                if g2g_x == 0 and g2g_y < 0: eular_angle = 3 * pi / 2

                rospy.loginfo("ANGLE: %f pi" %(eular_angle/pi))
                q_angle = quaternion_from_euler(0, 0, eular_angle,  axes='sxyz')
                q = Quaternion(*q_angle)
                goal.target_pose.pose.orientation = q

                self.move(goal)

                i += 1
            print('===========================================\n')
    
    # Initialize the marker point
    def init_markers(self):
        self.marker = Marker()
        self.marker.ns = 'waypoints'
        self.marker.id = 0
        self.marker.lifetime = rospy.Duration(0) # 0 is forever
        self.marker.type = Marker.SPHERE_LIST
        self.marker.action = Marker.ADD
        self.marker.scale.x = 0.15
        self.marker.scale.y = 0.15
        self.marker.color.r = 1.0
        self.marker.color.g = 0.7
        self.marker.color.b = 1.0
        self.marker.color.a = 1.0
        self.marker.header.frame_id = 'map'
        self.marker.header.stamp = rospy.Time.now()
        self.marker.points = []

    def move(self, goal):
        self.move_base.send_goal(goal)

        finished_within_time = self.move_base.wait_for_result(rospy.Duration(60))

        if not finished_within_time:
            self.move_base.cancel_goal()
            rospy.loginfo("Timed out achieving goal!")
        else:
            state = self.move_base.get_state()
            if state == GoalStatus.SUCCEEDED:
                rospy.loginfo("Goal succeeded!")
    
    def shutdown(self):
        rospy.loginfo("Stopping the tianbot_mini")
        self.move_base.cancel_goal()
        # Stop the tianbot
        self.cmd_vel_pub.publish(Twist())

if __name__ == '__main__':
    try:
        MultiMoveBase()
    except rospy.ROSInterruptException:
        pass