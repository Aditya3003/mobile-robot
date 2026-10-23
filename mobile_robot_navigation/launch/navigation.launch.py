import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    pkg_share = get_package_share_directory('mobile_robot_navigation')
    map_file = os.path.join(pkg_share, 'maps', 'room.yaml')
    nav2_params = os.path.join(pkg_share, 'config', 'nav2_params.yaml')

    # Nav2's own launch file: loads the map, localizes the robot on it (AMCL),
    # and starts path planning and driving
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch', 'bringup_launch.py')
        ),
        launch_arguments={
            'map': map_file,
            'params_file': nav2_params,
            'use_sim_time': 'true',
            'autostart': 'true',
        }.items(),
    )

    return LaunchDescription([nav2])