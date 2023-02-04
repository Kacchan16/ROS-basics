#!/usr/bin/env python
# license removed for brevity

import rospy
from std_msgs.msg import String

def talker():
  #create a new publisher, we specify topic name, type of message and then queue size
  pub = rospy.Publisher( 'chatter',std_msgs, queue_size=10)
  # after that we need to intialize the node
  # nodes names should be unique, if two nodes are same, previous node is out.
  # the anonymous=True flag means that rospy will chose a unique
  # name for our 'talker' node
  rospy.init_node('talker', anonymous=True)
  # set the loop rate
  rate= rospy.Rate(1) #Hz
  # it will publish until ctrl*C is piblished
  i=0
  while not rospy.is_shutdwom():
    hello_str = "hello robot %s" %i
    rospy.loginfo(hello_str)
    pub.publish(hello_str)
    rate.sleep()
    i=i+1
    
if __name__ == '__main__'
    try:
      talker()
    except rospy.ROSInterruptExecution:
      pass