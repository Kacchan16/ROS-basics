#!/usr/bin/env python

import rospy
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

def add_callback(message):
   rospy.loginfo("addition of two ints",%(message.a, message.b, (message.a+message.b)))
   #sum = message.a + message.b
   return AddTwoIntsResponse(message.a + message.b)
   

def add_two_ints_server():
   rospy.init_node('add_two_ints_server')
   s=rospy.Service( 'add_two_ints_topic', AddTwoInts, add_callback )
   #rate= rospy.Rate(1)
   rospy.loginfo("using service for addition of two ints")
   rosp.spin()
#while not rospy.is_shutdown():
 #  add_topic = AddTwoInts()
 

if __name__== "__main__":
    add_two_ints_server()