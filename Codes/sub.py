#!/usr/bin/env python   

import rospy 

from std_msgs.msg import String 

def print_message(msg): 

    rospy.loginfo(f"received:{msg.data}") 

    rospy.loginfo(msg)
    
def lab_subscriber1(): 

    rospy.init_node('RAA24_subnode') 
    
     
    sub=rospy.Subscriber("Greetings", String,print_message)  

    rospy.spin() 
if __name__=='__main__': 

    lab_subscriber1()