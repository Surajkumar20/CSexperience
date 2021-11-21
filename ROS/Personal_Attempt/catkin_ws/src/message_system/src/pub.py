#1/usr/bin/env python
import rospy as rp
from std_msgs.msg import String

def talker():
    pub = rp.Publisher('chatter', String, queue_size = 10)
    rp.init_nod('talker', anonymous = True)
    rate = rp.Rate(10)
    while not rp.is_shutdown():
        hello_str = "hello world {:s}".format(rp.get_time()) 
        rp.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()

if __name__ == "__main__":
    try:
        talker()
    except rp.ROSInterruptException:
        pass