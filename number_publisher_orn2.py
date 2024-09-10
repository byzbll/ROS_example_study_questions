#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

class NumberPublisher:
    def __init__(self):
        rospy.init_node("number_publisher_node", anonymous=True)
        self.pub = rospy.Publisher("fixed_number", Int32, queue_size=10)
        self.rate = rospy.Rate(1)

    def start_publishing(self):
        fixed_number = 5
        while not rospy.is_shutdown(): # parantez eksiği
            rospy.loginfo(f"Publishing: {fixed_number}")   
            self.pub.publish(fixed_number)
            self.rate.sleep() # rospy.rate.sleep() ==>> nooo
            
if __name__ == '__main__':
    try:
        publisher = NumberPublisher()
        publisher.start_publishing()
    except rospy.ROSInterruptException:
        pass       

