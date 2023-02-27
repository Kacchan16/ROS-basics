#!/usr/bin/env python
import rospy
import math
import time
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

def pose_callback(msg):
  global x,y,yaw
  x = msg.x
  y = msg.y
  yaw = msg.teta
  
def rotate (veloctiy_pub, angular_speed_degree, rel_angle_rot, is_cloclwise):
   rotate_mess= Twist()
   angular_speed= math.radians(abs(angular_speed_degree))
   if (is_cloclwise):
      velocity_pub.angular.z= -abs(angle_speed)
    else:
      velocity_pub.angular.z= abs(angle_speed)
     angle_moved=0.0
     loop_rate=rospy.Rate(10)
     velocity_pub=rospy.Publsiher('/turtle1/cmd_vel',Twist, queue_size=10)
     
     t0 = rospy.Time.now().to_sec()
    while True:
        rospy.loginfo("turtle rotates")
        velocity_pub.publish(rotate_mess)
        
        t1= rospy.Time.now().to_sec()
        current_angle_degree= (t1-t0)*angular_speed_degree
        loop_rate.sleep()
        
        if (current_angle_degree> relative_angle_degree):
           rospy.loginfo("reached")
           break
        rotate_mess.angular.z=0
        velocity_pub.publish(rotate_mess)
 
        
if __name__ == '__main__':
  try:
    rospy.init_node('ros_rotate_node',anonymous=True)
    velocity_pub = rospy.Publsiher('/turtle1/cmd_vel',Twist,queue_size=10)
    rotate_sub= rospy.Subscriber('/turtlesim/pose',Pose, pose_callback)
    rotate(velocity_pub,30,90,True)
   except rospy.ROSInterruptException:
      pass   
   