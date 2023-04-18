#inplace of rospy use rclpy
import rclpy
from Std_msgs.msg import String
from time import sleep

#little similar to cpp code

def talter(args=None):
   rclpy.init(args=args)
   node = rclpy.create_node('publisher_node')
   pub = node.create_publisher('chatter',String, 10)
   #rate=rospy.Rate(1)
   #inplace of rate, use time method
   msg = String()
   i=0
   while rclpy.ok():
      msg.data = "Hello world %d" %i
      i = i+1
      node.get_logger().info('publishing: "%s"' &msg.data)
      pub.publish(msg)
      sleep(0.5)
      
    node.destroy_node() 
    rclpy.shutdown()
    


if __name__ == '__main__':
    talker()
  
