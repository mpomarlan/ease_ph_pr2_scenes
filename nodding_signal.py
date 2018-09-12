#!/usr/bin/env python

import rospy
import tf.transformations
from geometry_msgs.msg import Twist
import numpy

def talker():
    pub = rospy.Publisher('/pr2/head_tilt_joint/cmd_vel', Twist, queue_size=10)
    #pub = rospy.Publisher('/r_shoulder_pan_velocity_controller/command', Twist, queue_size=10)
    rospy.init_node('nodding_signal', anonymous=True)
    f = 10.0
    rate = rospy.Rate(f) # 10hz
    t = 0.0
    while not rospy.is_shutdown():
        da_twist = Twist()
        da_twist.angular.x = 10*numpy.sin(2*3.14159*0.2*t)
        pub.publish(da_twist)
        rate.sleep()
        t += 1.0/f

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
