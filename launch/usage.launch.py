# SPDX-FileCopyrightText: 2024 Suzuha Kiuchi
# SPDX-License-Identifier: BSD-3-Clause
import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    cpu_usage = launch_ros.actions.Node(
            package='cpu_usage_ros2',
            executable='cpu_usage',
            )

    return launch.LaunchDescription([cpu_usage])
