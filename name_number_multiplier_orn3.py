#! /usr/bin/env python3

import rospy 
from std_msgs.msg import Int32, String

class NameNumberMultiplier:
    def __init__(self):
        rospy.init_node("name_number_multiplier_node", anonymous=True)
        self.fixed_number = None
        self.name_number = None
        self.name = None

        rospy.Subscriber("fixed_number", Int32, self.fixed_number_callback)
        rospy.Subscriber("name_string", String, self.name_callback)
        rospy.Subscriber("name_number", Int32, self.name_number_callback)

    def fixed_number_callback(self, data):
        self.fixed_number = data.data
        self.compute_product()

    def name_callback(self, data):
        self.name = data.data
        rospy.loginfo(f"Received name: {self.name}")

    def name_number_callback(self, data):
        self.name_number = data.data
        self.compute_product()
    
    def compute_product(self):
        if self.fixed_number is not None and self.name_number is not None:
            product = self.fixed_number * self.name_number
            rospy.loginfo(f"The product of {self.fixed_number} and {self.name_number} is {product}")
        if self.name:
            rospy.loginfo(f"Name: {self.name}")

    def start_listening(self):
        rospy.spin()      

if __name__ == '__main__':
    try:
        multiplier = NameNumberMultiplier()
        multiplier.start_listening()        
    except rospy.ROSInterruptException:
        pass    
