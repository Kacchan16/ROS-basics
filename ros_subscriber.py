#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback_function(message):
   rospy.loginfo(rospy.get_caller_id() + "I heard %s", message.data)

def listener():
   rospy.init_node('listener', anonymous=True)
   rospy.subscriber('chatter',String, callback_function)
   ros.spin()
   
if __name__ == '__main__'
    listener()