#!/usr/bin/env python

import rospy
import sys
from ros_essentials_cpp.srv import AddTwoInts
from ros_essentials_cpp.srv import AddTwoIntsRequest
from ros_essentials_cpp.srv import AddTwoIntsResponse

def add_two_ints_client(x,y):
  rospy.wait_for_service('add_two_ints_topic')
  try:
    add_two_ints_topic=rospy.ServiceProxy('add_two_ints_topic',AddTwoInts)
    resp1 = add_two_ints_topic(x,y)
   except rospy.ServiceException(e):
    print("service is failed : %s" %e)

def usage():
  return
  
if __name__=='__main__':
  if len(sys.argv) == 3:
     x == int(sys.argv[1])
     y == int(sys.argv[2])
   else:
     print("%s [x,y]", %sys.argv[0])
     sys.exit(1)
   print("requesting %s + %s", %(x.y))
   s = add_two_ints_client(x,y))
   print ("%s + %s = %s", %(x,y,s))