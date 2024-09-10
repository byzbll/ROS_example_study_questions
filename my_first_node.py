#! /usr/bin/env python3

import rospy
import rospy.logger_level_service_caller 


if __name__ == '__main__':
    rospy.init_node("test_node")
    rospy.loginfo("Test node has been started")

    rate = rospy.Rate(10)

    while not rospy.is_shutdown():
        rospy.loginfo("Hello")
        rate.sleep()

    # rospy.logwarn("This is a warning")
    # rospy.logerr("This is an error")

    # rospy.sleep(1.0)
    # rospy.loginfo("End of program") 