#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import math
import geometry_msgs.msg
from ros2_aruco_interfaces.msg import ArucoMarkers 

class ArTracker(Node):

    def __init__(self):
        super().__init__('ar_tracker')
        timer_period = 0.1  # seconds
        self.isEmptyMarkerList = True
        self.angular = 0.0
        self.linear = 0.0
        self.ar_pose = geometry_msgs.msg.Pose()

        ### SUBSCRIPTION TO AR POSE ID DETECTOR
        
        # Use create_subscription 
        ## Arguments
        ### 1) Use the imported Message Type for AR marker
        ### 2) Find the topic name which publishes AR info
        ### 3) Create a Callback to retrieve pose
        ### 4) Set Queue Size to 10
        
        # Edit Here
        
        # self.subscription  # prevent unused variable warning

        # Create Publisher to command velocity
        # Edit Here
        
        # Create Timer to run cmd_vel_timer_callback function {use above timer period}
        # Edit Here

        # Create Timer to run chase tag function {use above timer period}
        # Edit Here
        

    
  #  def cmd_vel_timer_callback(self):
        # Assign Command Velocity
        # Edit Here

        # Assign Computed Linear and Angular Velocity
        # cmd.linear.x = # Edit Here
        # cmd.angular.z = # Edit Here
        
        # Publish the Command Velocity
        # self.publisher_.publish(cmd)

    def check_if_visible_callback(self, data):
        # If the markers list is empty, isEmptyMarkerList = True
        if not data.poses:
            self.isEmptyMarkerList = True
        else:
            self.isEmptyMarkerList = False
            
            # Retrieve the First ArUco Pose
            # Edit Here

    # Function to compute velocity to chase the AR tag
    def chase_tag(self):
    
        # Use Right Hand Rule and Consider Camera/Tag Coordinate Frame
        # to Retrive the right position coordinate for x and y translation
        
        #trans_x = # Edit Here
        #trans_y = # Edit Here

        # Do not move if no ar_tag found
        if self.isEmptyMarkerList == True:
            self.angular = 0.0
            self.linear = 0.0

        # Compute velocity required to chase tag based on distance and orientation from tag
        # Write Proportinal Controller equation to reduce angular error and translational error
        # Tune to proportional gain to achieve better tracking
        
        #else:
            # Edit Here

        print("Angular: " + str(self.angular))
        print("Linear: " + str(self.linear))


def main(args=None):
    rclpy.init(args=args)
    print("AR Tracking!")
    
    # Initialize node object by calling the Class
    # Edit Here

    # Spin the node 
    # Edit Here

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    # Edit Here
    rclpy.shutdown()


if __name__ == '__main__':
    main()
