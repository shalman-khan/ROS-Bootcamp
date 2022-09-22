import rclpy
import time
from threading import Thread
from rclpy.executors import SingleThreadedExecutor, MultiThreadedExecutor
from rclpy.node import Node
# Message Interface Imports
from geometry_msgs.msg import Twist
from nav_msgs.msg import Odometry
from sensor_msgs.msg import LaserScan
# Transformations for ROS2
import tf_transformations
from rclpy.callback_groups import MutuallyExclusiveCallbackGroup, ReentrantCallbackGroup
from rclpy.qos import QoSProfile, QoSReliabilityPolicy, QoSHistoryPolicy

#Declaring Global Variables
maxpos = 0 
yaw = 0
turnindex = 0

class MazeNav(Node):
    def __init__(self):
        # Class Constructor
        super().__init__('maze_nav')

        reentrant_callback_group = ReentrantCallbackGroup()
        timer_cb_group = MutuallyExclusiveCallbackGroup()
        
        # Twist: Publisher Object [Queue Size : 1]
        self.cmd_vel_pub = self.create_publisher(Twist, 'cmd_vel', 1)
        # Laser Scan: Subscriber Object
        self.laser_subscriber = self.create_subscription(
            LaserScan, '/scan', self.scan_callback, QoSProfile(depth=1, reliability=QoSReliabilityPolicy.BEST_EFFORT),callback_group=reentrant_callback_group)
        # Odometry: Subscriber Object
        self.odom_subscriber = self.create_subscription(
            Odometry, '/odom', self.odom_callback, QoSProfile(depth=1, reliability=QoSReliabilityPolicy.BEST_EFFORT),callback_group=reentrant_callback_group)

        # Variable Declaration
        self.laser_subscriber
        self.odom_subscriber
        self.turnindex = 0
        # define the timer period for 0.5 seconds
        self.timer_period = 0.5
        # define the variable to save the received info
        self.laser_forward = 0
        # Twist message: Definition
        self.command = Twist()
        self.command.linear.x = 0.0
        self.command.linear.z = 0.0

        self.motion_freq = 0.05
        self.motion_timer = self.create_timer(self.motion_freq, self.nav_motion, callback_group=timer_cb_group)

    # Function for odom_callback

    def scan_callback(self, msg):
        global range_front
        global range_right
        global range_left
        global ranges
        global maxpos

        # Obtain Range from the Front, Right and Left
        range_front = msg.ranges[0]
        range_right = msg.ranges[270]
        range_left = msg.ranges[90]

        # Obtain the Furthest Distance odom_callback
        ranges = [range_front, range_right, range_left]
        maxpos = ranges.index(max(ranges)) + 1

    # Function for Orientation

    def odom_callback(self, msg2):
        global yaw

        # Obtain Quaternion Orientation
        quaternion = (msg2.pose.pose.orientation.x, msg2.pose.pose.orientation.y,
                      msg2.pose.pose.orientation.z, msg2.pose.pose.orientation.w)
        # Transform Quaternion to Euler coordinate system
        euler = tf_transformations.euler_from_quaternion(quaternion)
        yaw = euler[2]

        # Transform Yaw into 360 degrees format
        if (yaw < 0):
            yaw += 6.28319

    def nav_motion(self):
        global maxpos
        global yaw

        ###########  GO FORWARD   ##################
        # Edit Here
        

        ############################################
        ###########  TURN RIGHT  ###################
        # Edit Here
        

        ############################################
        ###########  TURN LEFT  ###################
        # Edit Here
        

def main(args=None):
    rclpy.init()
    node = MazeNav()
    executor = MultiThreadedExecutor()
    executor.add_node(node)

    try:
        node.get_logger().info('Beginning client, shut down with CTRL-C')
        executor.spin()
    except KeyboardInterrupt:
        node.get_logger().info('Keyboard interrupt, shutting down.\n')
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    
