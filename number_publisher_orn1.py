#! /usr/bin/env python3

import rospy 
from std_msgs.msg import Int32
import random

class NumberPublisher:
    def __init__(self):
        rospy.init_node("number_publisher_node", anonymous=True)
        self.pub = rospy.Publisher("random_number", Int32, queue_size=10)
        self.rate = rospy.Rate(1) # 1 Hz
 
    def start_publishing(self): 
        while not rospy.is_shutdown():
            random_number = random.randint(0, 100)
            rospy.loginfo(f"Publishing: {random_number}")
            self.pub.publish(random_number)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        publisher = NumberPublisher()
        publisher.start_publishing()
    except rospy.ROSInterruptException:
        pass             
