#!/usr/bin/env python

import ropsy
from ros_essentials_cpp import Bio

def bio_callback(message):
   rospy.loginfo( rospy.get_caller_id() + "I got information %s" , (%s, %i, %.2f, %.2f), message.name, message.age, message.temperature, message.humidity)
   
rospy.init__node('bio_listener_node', anonymous=True)
rospy.Subcriber('bio_topic',Bio, bio_callback)
rospy.spin()