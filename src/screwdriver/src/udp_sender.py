#!/usr/bin/env python

# References
# ----------
# https://andrewdai.co/xbox-controller-ros.html#rosjoy

import rospy
import socket
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

UDP_IP = "192.168.0.178"
UDP_PORT = 30010

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT

def callback(msg):
    global pose
    pose = msg

    rotation_speed_double = pose.linear.x
    rotation_speed_int = int(255*rotation_speed_double)

    Message = "%d"%(rotation_speed_int)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(Message, (UDP_IP, UDP_PORT))
    
if __name__ == '__main__':
    rospy.init_node("ros_udp_client")
    pub = rospy.Publisher("test_vel", Twist, queue_size=1)
    rospy.Subscriber("screw_vel", Twist, callback)
    rate = rospy.Rate(10)
    twist = Twist()

    while not rospy.is_shutdown():
        pub.publish(twist)
        rate.sleep()
