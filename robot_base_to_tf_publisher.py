#!/usr/bin/env python

import rospy
import tf.transformations
from geometry_msgs.msg import PoseStamped, TransformStamped
from tf2_msgs.msg import TFMessage

def callback(pub, data):
    da_tf = TFMessage()
    base_transform = TransformStamped()
    base_transform.header.stamp = data.header.stamp
    base_transform.header.frame_id = "odom"
    base_transform.child_frame_id = "base_footprint"
    base_transform.transform.translation.x = data.pose.position.x
    base_transform.transform.translation.y = data.pose.position.y
    base_transform.transform.translation.z = data.pose.position.z
    base_transform.transform.rotation.x = data.pose.orientation.x
    base_transform.transform.rotation.y = data.pose.orientation.y
    base_transform.transform.rotation.z = data.pose.orientation.z
    base_transform.transform.rotation.w = data.pose.orientation.w
    da_tf.transforms = [base_transform]
    pub.publish(da_tf)
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('robot_base_to_tf_publisher', anonymous=True)

    pub = rospy.Publisher('/tf', TFMessage, queue_size=10)

    rospy.Subscriber("/pr2/base_pose", PoseStamped, lambda x: callback(pub, x))

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass


