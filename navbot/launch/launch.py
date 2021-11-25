import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument,ExecuteProcess
from launch.actions import IncludeLaunchDescription
from launch.substitutions import Command
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    package_dir = get_package_share_directory('navbot')
    xacro = os.path.join(package_dir,'rover.xacro')
    urdf = os.path.join(package_dir,'rover.urdf')
    
    rviz_config = os.path.join(package_dir,'config.rviz')


    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'),
       Node(
           package='robot_state_publisher',
           executable='robot_state_publisher',
           name='robot_state_publisher',
           output='screen',
           parameters = [{'use_sim_time':True,'robot_description':Command(['xacro ',xacro])}],
           arguments = [urdf]
       ),
    
       
      
       Node(
           package='rviz2',
           executable='rviz2',
           name='rviz2',
           output='screen',
           arguments=['-d',rviz_config]
           ),
       
        
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            name='urdf_spawner',
            output='screen',
            arguments=["-topic", "/robot_description", "-entity", "rover"])
    ])


