#!/usr/bin/env python

import rospy
from sensor_msgs.msg import JointState

def callback(pub, data):
    data.header.stamp = rospy.get_rostime()
    #data.header.stamp = rospy.Time()
    data.header.frame_id = ''
    pub.publish(data)

def listener():

    rospy.init_node('joint_state_retiming', anonymous=True)

    pub = rospy.Publisher('/joint_states', JointState, queue_size=10)

    rospy.Subscriber("/unity_joint_states", JointState, lambda x: callback(pub, x))

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
 
