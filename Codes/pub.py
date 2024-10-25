#!/usr/bin/python3

import rospy 
from std_msgs.msg import String

def lab_publisher1(): 
    rospy.init_node('pooja_node1',anonymous=True) 

    pub = rospy.Publisher('Greetings', String, queue_size=10) 

    rate = rospy.Rate(10) 
    
    
    while not rospy.is_shutdown(): 
        msg = String()
        txt="Hello,I am Pooja" 
        msg.data=txt
        pub.publish(msg)
        rospy.loginfo(txt)
        
        rate.sleep() 


if __name__=='__main__':
    try:
        lab_publisher1() 
    except rospy.ROSInterruptException: 
        
        pass