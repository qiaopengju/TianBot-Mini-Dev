#!/usr/bin/env python
# control the linear speed and angular speed of the bot

import rospy
from geometry_msgs.msg import PoseStamped, Point, Pose
from visualization_msgs.msg import Marker

def goal_as():
    goal_pub = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
    marker_pub = rospy.Publisher('waypoint_markers', Marker, queue_size=10)
    rospy.init_node('goal_as', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        goal = PoseStamped()
        while True:
            xx = input('Goal Pos X: ')
            if type(xx) == float or type(xx) == int: break
            else:
                print('Position.x must be float, input again!\n')
        while True:
            yy = input('Goal Pos Y: ')
            if type(yy) == float or type(yy) == int: break
            else:
                print('Position.y must be float, input again!\n')

        goal.pose.position.x = xx
        goal.pose.position.y = yy
        goal.pose.orientation.w = 1.0
        goal.header.frame_id = 'map'

        goal_pub.publish(goal)

        # Initialize the marker point
        marker = Marker()
        marker.ns = 'waypoints'
        marker.id = 0
        marker.lifetime = rospy.Duration(0) # 0 is forever
        marker.type = Marker.SPHERE_LIST
        marker.action = Marker.ADD
        marker.scale.x = 0.15
        marker.scale.y = 0.15
        marker.color.r = 1.0
        marker.color.g = 0.7
        marker.color.b = 1.0
        marker.color.a = 1.0
        marker.header.frame_id = 'map'
        marker.header.stamp = rospy.Time.now()
        marker.points = [Pose(goal.pose.position, goal.pose.orientation).position]
        marker_pub.publish(marker)

        rate.sleep()
        print("=============\n")

if __name__ == '__main__':
    try:
        goal_as()
    except rospy.ROSInterruptException:
        pass