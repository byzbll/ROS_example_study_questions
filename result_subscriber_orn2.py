#! /usr/bin/env python3

import rospy
from std_msgs.msg import Int32

class ResultSubscriber:
    def __init__(self):
        rospy.init_node("result_subscriber_node", anonymous=True)
        self.sub = rospy.Subscriber("multiplied_number", Int32, self.callback)

    def callback(self, data):
        rospy.loginfo(f"Result: {data.data}")

    def start_listening(self):
        rospy.spin()

if __name__ == '__main__':
    try:
        subscriber = ResultSubscriber()
        subscriber.start_listening()
    except rospy.ROSInterruptException:
        pass    

