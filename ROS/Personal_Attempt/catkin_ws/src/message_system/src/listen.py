#!/usr/bin/env python
import rospy as rp
from std_msgs.msg import String

def callback(data):
    rp.loginfo(rp.get_caller_id() + "I heard {}".format(data.data))

def listener():
    rp.init_node('listener', anonymous = True)
    rp.Subscriber("catter", String, callback)
    rp.spin()

if __name__ == "__main__":
    listener()