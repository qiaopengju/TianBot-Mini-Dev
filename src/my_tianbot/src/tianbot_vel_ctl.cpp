#include <stdio.h>
#include <termios.h>
#include "ros/ros.h"
#include "geometry_msgs/Twist.h"

int main(int argc, char **argv)
{
    ros::init(argc, argv, "vel_ctl");
    ros::NodeHandle n;
    //ros::Publisher publisher = n.advertise<geometry_msgs::Twist>("turtlesim1/turtle1/cmd_vel", 1000);
    ros::Publisher publisher = n.advertise<geometry_msgs::Twist>("tianbot_mini/cmd_vel", 1000);
    ros::Rate loop_rate(60);

    // 不用回车输入 
    static struct termios oldt, newt;
    tcgetattr(STDIN_FILENO, &oldt);
    newt = oldt;
    newt.c_lflag &= ~(ICANON);
    tcsetattr(STDIN_FILENO, TCSANOW, &newt);
    
    // 打印输入提示
    printf( "Reading from the keyboard  and Publishing to Twist!\n"
                    "---------------------------\n"
                    "Quit: 'q'\n"
                    "Moving around:\n"
                    "u    i    o\n"
                    "j    k    l\n"
                    "m    ,    .\n");
    while(ros::ok())
    {
        geometry_msgs::Twist vel;
        system("stty -echo"); // don't display input
        char token = getchar(); // get token
        system("stty echo"); // display input

        // // 处理键盘输入
        switch (token)
        {
            case 'i':  vel.linear.x = 0.1; break;
            case 'k':  vel.linear.x = -0.1; break;
            case 'j':  vel.linear.y = 0.1; break;
            case 'l':  vel.linear.y = -0.1; break;
            case 'u':  vel.angular.z = 0.5; break;
            case 'o':  vel.angular.z = -0.5; break;
            case 'q': return 0;
            default: break;
        }
        // 圆周运动
        // vel.linear.x = 0.2;
        // vel.angular.z = 1.0;
        publisher.publish(vel);
        loop_rate.sleep();
    }
    tcsetattr(STDIN_FILENO, TCSANOW, &oldt);

    return 0;
}