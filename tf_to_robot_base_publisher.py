#!/usr/bin/env python

import rospy
import math
import tf
from geometry_msgs.msg import PoseStamped, TransformStamped
from tf2_msgs.msg import TFMessage

if __name__ == '__main__':
    try:
        rospy.init_node('tf_to_robot_base_publisher', anonymous=True)

        odom = 'odom'
        if rospy.has_param('odom_frame'):
            odom = rospy.get_param('odom_frame')
        robot = 'base_footprint'
        if rospy.has_param('root_frame'):
            odom = rospy.get_param('root_frame')

        listener = tf.TransformListener()
        pub = rospy.Publisher('/pr2/base_pose', PoseStamped, queue_size=10)

        rate = rospy.Rate(10.0)
        while not rospy.is_shutdown():
            try:
                (trans,rot) = listener.lookupTransform(odom, robot, rospy.Time(0))
                da_pose=PoseStamped()
                da_pose.header.stamp = rospy.get_rostime()
                da_pose.header.frame_id = odom
                da_pose.pose.position.x = trans[0]
                da_pose.pose.position.y = trans[1]
                da_pose.pose.position.z = trans[2]
                # Some weird things happening with rotations in Unity, so do some rearrangement
                da_pose.pose.orientation.x = rot[1]
                da_pose.pose.orientation.y = rot[0]
                da_pose.pose.orientation.z = rot[2]
                da_pose.pose.orientation.w = -rot[3]
                pub.publish(da_pose)
            except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
                continue
            rate.sleep()
    except rospy.ROSInterruptException:
        pass


