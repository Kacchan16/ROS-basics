#!/usr/bin/env python
import rospy
from ros_essentials_cpp.msg import IotSensor
import random

def data():
   pub= rospy.Publisher('iot_sensor_topic', IotSensor, queue_size=10)
   rospy.init_node('iot_publsiher_node', anonymous=True)
   rate=rospy.Rate(1)
   i=0
   
   while not rospy.is_shutdown():
     iot_sensor = IotSensor()
     iot_sensor.id = 1
     iot_sensor.name = 'number one'
     iot_sensor.temperature = 27.92 + (random.random()*2)
     iot_sensor.humidity = 26.32 + (random.ranodm()*2)
     rospy.loginfo("I am publishing")
     rospy.loginfo(iot_sensor)
     pub.Publish(iot_sensor )
     rate.sleep()
     i = i+1
     
if __name__ == '__main__':
   try:
     data()
   except rospy.ROSInterrupException:
     pass