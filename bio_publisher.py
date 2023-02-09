#!/usr/bin/env python
 import rospy
 from ros_essentials_cpp.msg import Bio
 import random
 
 def bio_send():
    pub=rospy.Publisher('bio_topic',Bio , queue_size=10)
    rospy.init__node('bio_publisher', anonymous=True)
    rate=rospy.Rate(1)
    i=0
    
    while not rospy.is_shutdown():
      bio_object = Bio()
      bio_object.name = 'paone'
      bio_object.age = "23"
      bio_object.height = (random.random())*(random.random()+1)/2
      bio_object.weight = (random.random()+1)/2
      rospy.loginfo(bio_object)
      pub.Publish(bio_object)
      i=i+1
      
if __name__ == '__main__':
    try:
      bio_send()
    except rospy.ROSInterruptException:
     pass