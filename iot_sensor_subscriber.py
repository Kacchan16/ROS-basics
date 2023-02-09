#!/usr/bin/env python

import rospy
from ros_essentials_cpp import IotSensor

def callbackfunction(message):
   rospy.loginto( "new Iot data received: (%d, %s, %.2f ,%.2f)", message.id, message.name, message.temperature, message.humidity)

def listener():
   rospy.init__node('iot_subscriber_node', anonymous=Ture)
   rospy.Subscriber('iot_sensor_topic',IotSensor, callbackfunction)
   rospy.spin()
   
if __name__='__main__':
      listener()
   