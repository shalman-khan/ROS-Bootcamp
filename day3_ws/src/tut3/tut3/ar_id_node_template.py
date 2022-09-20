#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math
import geometry_msgs.msg
from ros2_aruco_interfaces.msg import ArucoMarkers 

class ArIdentifier(Node):

    def __init__(self):
        super().__init__('ar_identfier')

        self.ar_id = None
        self.ar_pose = geometry_msgs.msg.Pose()

        ### SUBSCRIPTION TO AR POSE ID DETECTOR
        
        # Use create_subscription 
        ## Arguments
        ### 1) Use the imported Message Type for AR marker
        ### 2) Find the topic name which publishes AR info
        ### 3) Create a Callback to store & print id and pose
        ### 4) Set Queue Size to 10
        
        ## EDIT HERE

        # self.subscription  # prevent unused variable warning

    def id_and_pose_callback(self, data):
        ### CALLBACK FUNCTION FOR AR POSE ID DETECTOR
        
        # Use "ros2 interface show <message type>" to identify necessary attribute
        # Identify attribute for pose and attribute for marker id
        # store the variables and print 
        # Optional [Check for pose before printing]
        
        #if poses avaiable: #EDIT HERE
        #    self.ar_pose = #EDIT HERE
        #    self.ar_id = #EDIT HERE
            print("AR TAG DETECTED ID: ", self.ar_id)
            print(f" Pose Information: ", self.ar_pose)

def main(args=None):
    rclpy.init(args=args)
    print("AR Pose and ID Tracking!")

    # Initialize node object by calling the Class
    #EDIT HERE

    # Spin the node 
    #EDIT HERE

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    #EDIT HERE
    rclpy.shutdown()


if __name__ == '__main__':
    main()
