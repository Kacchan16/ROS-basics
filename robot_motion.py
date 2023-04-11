#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time
from std_srvs.srv import Empty

x=0
y=0
z=0
yaw=0

def pose_callback(pose_msg):
   global x,y,z,yaw
   x=pose_msg.x
   y=pose_msg.y
   yaw=pose_msg.yaw
   
def move(speed, distance):
   velocity_msg=Twist()
   x0=x
   y0=y
   velocity_msg.linear.x=speed
   distance_covered=0.0
   loop_rate=rospy.Rate(10)
   velocity_pub = rospy.publisher('turtle1/cmd_vel',Twist, queue_size=10)
   
    while True:
         rospy.loginfo("Turtle moving forward")
         veloctiy_pub.publish(velocity_msg)
         loop_rate.sleep()
         
         distance_covered= distance_covered + abs(0.5*math.sqrt(((x-x0)**2)+((y0-y)**2)))
         printdistance_covered)
         if not (distance_covered<distance):
            rospy.loginfo("goal reached")
            break
    velocity_msg.linear.x=0
    velocity_msg.publish(velocity_msg)
    
if __name__ =='__main__':
  try:
    rospy.init_node('turtle_movement', anonymous=True)
    velocity_pub = rospy.publisher('turtle1/cmd_vel', Twist, queue_size=10)
    pose_subscriber= rospy.subscriber('/turtle1/pose', Pose, pose_callback)
    
    time.sleep(2)
    print("move")
    move(1.0, 5.0)
    time.sleep(2)
    print('start reset: ')
    rospy.wait_for_service('reset')
    reset_turtle = rospy.ServiceProxy('reset', Empty)
    reset_turtle()
    print('end result: ')
    rospy.spin()
    
  except rospy.ROSInterruptExecution:
     rospy.loginfo("node terminated")