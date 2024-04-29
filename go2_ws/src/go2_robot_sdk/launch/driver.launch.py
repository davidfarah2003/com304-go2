import os
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    robot_ip = LaunchConfiguration('robot_ip', default=os.getenv('ROBOT_IP'))
    robot_token = LaunchConfiguration('robot_token', default=os.getenv('ROBOT_TOKEN',''))
    
    return LaunchDescription([
        Node(
            package='go2_robot_sdk',
            executable='go2_movement_driver_node',
            parameters=[{'robot_ip': robot_ip, 'token': robot_token}],
            ),
    ])