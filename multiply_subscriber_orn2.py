#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

class MultiplySubscriber:
    def __init__(self, multiplier):
        self.multiplier = multiplier # sabit sayı
        rospy.init_node("multiply_subscriber_node", anonymous=True)
        self.sub = rospy.Subscriber("fixed_number", Int32, self.callback)
        self.pub = rospy.Publisher("multiplied_number", Int32, queue_size=10)

    def callback(self, data):
        result = data.data * self.multiplier
        rospy.loginfo(f"Multiplying {data.data} by {self.multiplier} to get {result}")
        self.pub.publish(result) # rospy.pub.publish(result)
   
    def start_listening(self):
        rospy.spin()

if __name__ == '__main__':
    try:
       multiplier = 7
       subscriber = MultiplySubscriber(multiplier)
       subscriber.start_listening()
    except rospy.ROSInterruptException:
        pass
        

