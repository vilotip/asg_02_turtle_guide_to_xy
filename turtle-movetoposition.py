#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import time

current_x = 0.0
current_y = 0.0
current_theta = 0.0

def function(data):
    global current_x
    global current_y
    global current_theta
    current_x = data.x
    current_y = data.y
    current_theta = data.theta
    
rospy.init_node("turtle_guide_to_xy")
pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)
rospy.Subscriber("/turtle1/pose", Pose, function)

#x = float(input("Enter target x: "))
#y = float(input("Enter target y: "))
#radius_th = float(input("Enter radius threshold: "))
x=float(rospy.get_param('x'))
y=float(rospy.get_param('y'))
center_x = 5.54
center_y = 5.54
target_x = x - center_x #zeroing at center
target_y = y - center_y #zeroing at center
distance = math.sqrt(target_x**2 + target_y**2)
print(target_x,target_y)
angle = math.atan(target_y/target_x)
print(distance,angle)
msg=Twist()

while not rospy.is_shutdown():
   
    if target_x > 0.0 and target_y > 0.0:
        while current_theta <= angle:
            msg.linear.x = 0.0
            msg.angular.z = angle
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)
        msg.angular.z = 0.0
        pub.publish(msg) 
        while current_x < center_x+(distance*math.cos(angle)):
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.linear.x = 0.0
        pub.publish(msg)
        rospy.loginfo("Target Reached") 
        
    elif target_x < 0.0 and target_y < 0.0:
        while current_theta <= angle:
            msg.linear.x = 0.0
            msg.angular.z = angle
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.angular.z = 0.0
        pub.publish(msg) 
        while current_x > center_x-(distance*math.cos(angle)):
            msg.linear.x = -0.2
            msg.angular.z = 0.0
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.linear.x = 0.0
        pub.publish(msg) 
        rospy.loginfo("Target Reached") 
        
    elif target_x > 0.0 and target_y < 0.0:
        while current_theta > angle:
            msg.linear.x = 0.0
            msg.angular.z = angle
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.angular.z = 0.0
        pub.publish(msg) 
        while current_x < center_x+(distance*math.cos(angle)):
            msg.linear.x = 0.2
            msg.angular.z = 0.0
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.linear.x = 0.0
        pub.publish(msg) 
        rospy.loginfo("Target Reached")         
        
    elif target_x < 0.0 and target_y > 0.0:
        while current_theta > angle:
            msg.linear.x = 0.0
            msg.angular.z = angle
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.angular.z = 0.0
        pub.publish(msg) 
        while current_x > center_x-(distance*math.cos(angle)):
            msg.linear.x = -0.2
            msg.angular.z = 0.0
            pub.publish(msg)
            time.sleep(0.1)
            rospy.logdebug("%f,%f,%f", current_x, current_y, current_theta)
            rospy.loginfo("Moving to %f,%f", x, y)            
        msg.linear.x = 0.0
        pub.publish(msg)
        rospy.loginfo("Target Reached")         

      
    

