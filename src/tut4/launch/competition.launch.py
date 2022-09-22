import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription, ExecuteProcess
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node 
from launch_ros.substitutions import FindPackageShare

TURTLEBOT3_MODEL = os.environ['TURTLEBOT3_MODEL']


def generate_launch_description():
    x_pos = LaunchConfiguration('x_pos', default='0.0')
    y_pos = LaunchConfiguration('y_pos', default='-0.0')
    z_pos = LaunchConfiguration('z_pos', default='0.0')
    roll = LaunchConfiguration('roll', default='0')
    pitch = LaunchConfiguration('pitch', default='0')
    yaw = LaunchConfiguration('yaw', default='0')

    world = LaunchConfiguration('world')
    paused = LaunchConfiguration('paused', default='false')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    gui = LaunchConfiguration('gui', default='true')
    headless = LaunchConfiguration('headless', default='false')
    debug = LaunchConfiguration('debug', default='false')    

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    world_file_name = 'competition.model'
    world_path = os.path.join(get_package_share_directory('tut4'),
                         'worlds', world_file_name)

    gazebo_models_path = os.path.join(pkg_gazebo_ros, 'models')
    os.environ["GAZEBO_MODEL_PATH"] = gazebo_models_path

    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            arguments = ["-1.95", "-0.55", "2.0", "-1.58", "0", "-1.58", "odom", "camera_link"],
            name='camera_tf'
        ),

        DeclareLaunchArgument(
            name='world',
            default_value=world_path,
        ),
         
        DeclareLaunchArgument(
            name='paused',
            default_value='false'
        ),
     
        DeclareLaunchArgument(
            name='use_sim_time',
            default_value='true'
        ),
     
        DeclareLaunchArgument(
            name='gui',
            default_value='true'
        ),

        DeclareLaunchArgument(
            name='headless',
            default_value='false'
        ),

        DeclareLaunchArgument(
            name='debug',
            default_value='false'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
            ),
            launch_arguments={'world': world}.items(),
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
            ),
        )

        Node(
            package='gazebo_ros', 
            executable='spawn_entity.py',
            arguments=[
                '-urdf', '', 
                '-entity', 'turtlebot3_burger',
                '-x', x_pos, 
                '-y', y_pos, 
                '-z', z_pos, 
                '-R', roll, 
                '-P', pitch, 
                '-Y', yaw, 
                '-file', 'robot_description', 
            ],
            output='screen',
            name='spawn_urdf'
        )
    ])
