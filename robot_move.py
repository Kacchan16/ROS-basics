#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg):
  global x,y,yaw
  x= msg.x
  y= msg.y
  yaw = msg.teta
 # return x,y,yaw

def striaght(velocity_pub, speed, distance,is_forward):
   veolcity_m = Twist()
   global x,y
    x0=x
    y0=y
    
   if (is_forward):
      velocity_m.linear.x= abs(speed)
    else:
      velocity_m.linear.x= -abs(speed)
    
     distance_moved=0.0
     loop_rate = rospy.rate(10)
     
     while True:
        rospy.loginfo("turtle going forward")
        velocity_pub.publsih(velocity_m)
        loop_rate.sleep()
         distance_moved = abs(math(sqrt (((x0-x)^2)+((y0-y)^2))))
         print( distance_moved)
         print(x)
         if not(dist_moved< distance):
           rospy.loginfo("reached goal")
           break
      velocity_m.linear.x=0
      velocity_pub.publsiher(velocity_m)
     
    
if __name__ == '__main__':
   rospy.init_node('ros_movement_node', anonymous=True)
   velocity_pub = rospy.Publisher('/turtle1/cmd_vel',Twist,queue_size=10)
   pose_sub = rospy.subscriber('/turlesim/pose',Pose, pose_callback)
   velocity_pub.publish(velocity_m)
   straight(velocity_pub,2,4,True)