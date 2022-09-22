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

        # Subscription to AR pose detector
        self.subscription = self.create_subscription(
            ArucoMarkers,
            '/aruco_markers',
            self.check_if_visible_callback,
            10)
        self.subscription  # prevent unused variable warning

        # Publisher to command velocity
        self.publisher_ = self.create_publisher(geometry_msgs.msg.Twist, 'cmd_vel', 10)
        self.cmdvel_timer = self.create_timer(timer_period, self.cmd_vel_timer_callback)

        # Function to compute velocity to chase the AR tag
        self.chase_tag_computation_timer = self.create_timer(timer_period, self.chase_tag)
        

    
    def cmd_vel_timer_callback(self):
        cmd = geometry_msgs.msg.Twist()

        cmd.linear.x = self.linear
        cmd.angular.z = self.angular
        self.publisher_.publish(cmd)

    def check_if_visible_callback(self, data):
        # If the markers list is empty, isEmptyMarkerList = True
        if not data.poses:
            self.isEmptyMarkerList = True
        else:
            self.isEmptyMarkerList = False
            self.ar_pose = data.poses[0] # First aruco pose

    def chase_tag(self):
        trans_x = self.ar_pose.position.z
        trans_y = self.ar_pose.position.x

        # Do not move if no ar_tag found
        if self.isEmptyMarkerList == True:
            self.angular = 0.0
            self.linear = 0.0

        # Compute velocity required to chase tag based on distance and orientation from tag
        else:
            self.angular = -0.2*math.atan2(trans_y,trans_x)
            self.linear =  0.1*(math.sqrt(trans_x**2) - 0.5)

        print("Angular: " + str(self.angular))
        print("Linear: " + str(self.linear))


def main(args=None):
    rclpy.init(args=args)
    print("AR Tracking!")

    ar_tracker = ArTracker()

    rclpy.spin(ar_tracker)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ar_tracker.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()