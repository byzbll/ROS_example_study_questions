#! /usr/bin/env python3

import rospy 
from std_msgs.msg import Int32, String

class NameNumberPublisher:
    def __init__(self):
        rospy.init_node("name_number_publisher_node", anonymous=True)
        self.string_pub = rospy.Publisher("name_string", String, queue_size=10)
        self.number_pub = rospy.Publisher("name_number", Int32, queue_size=10)
        self.rate = rospy.Rate(1)

    def start_puplishing(self):
        name = 'Beyza'
        number = 3
        while not rospy.is_shutdown():
            rospy.loginfo(f"Publishing name: {name} and number: {number}")  
            self.string_pub.publish(name)  
            self.number_pub.publish(number)
            self.rate.sleep()

if __name__ == '__main__':
    try:
        publisher = NameNumberPublisher()
        publisher.start_puplishing()        
    except rospy.ROSInterruptException:
        pass    
