#!/usr/bin/env python
# control the linear speed and angular speed of the bot

import rospy
from geometry_msgs.msg import  Twist

def my_vel_ctr():
    pub = rospy.Publisher('turtlesim1/turtle1/cmd_vel', Twist, queue_size=10)
    rospy.init_node('my_vel_ctr', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    print("""
Reading from the keyboard  and Publishing to Twist!
 ---------------------------
 Moving around:
 u    i    o
 j    k    l
 m    ,    .""")
    while not rospy.is_shutdown():
        move_cmd = Twist()
        # keyboard input
        token =  raw_input()
        # linear speed control
        if token.upper() == 'I':
            move_cmd.linear.x = 1.0
        elif token.upper() == 'K':
            move_cmd.linear.x = -1.0
        elif token.upper() == 'J':
            move_cmd.linear.y = 1.0
        elif token.upper() == 'L':
            move_cmd.linear.y = 1.0
        # angular speed control
        elif token.upper() == 'U':
            move_cmd.angular.z = 0.5
        elif token.upper() == 'O':
            move_cmd.angular.z = -0.5

        rospy.loginfo(token)
        pub.publish(move_cmd)
        rate.sleep()

if __name__ == '__main__':
    try:
        my_vel_ctr()
    except rospy.ROSInterruptException:
        pass