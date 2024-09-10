#! /usr/bin/env python3

import rospy 
from std_msgs.msg import Int32

class FixedNumberPublisher:
    def __init__(self):
        rospy.init_node("fixed_number_publisher_node", anonymous=True)
        self.pub = rospy.Publisher("fixed_number", Int32, queue_size=10)
        self.rate = rospy.Rate(1)

    def start_publishing(self):
        fixed_number = 3
        while not rospy.is_shutdown():
            rospy.loginfo(f"Publishing fixed number: {fixed_number}")
            self.pub.publish(fixed_number)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        publisher = FixedNumberPublisher()            
        publisher.start_publishing()
    except rospy.ROSInterruptException:
        pass    

