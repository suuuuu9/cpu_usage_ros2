#!/bin/bash
# SPDX-FileCopyrightText: 2025 Suzuha Kiuchi
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws
colcon build
source $dir/.bashrc
timeout 10 ros2 launch cpu_usage_ros2 usage.launch.py | tee -i /tmp/cpu_usage_ros2.log

cat /tmp/cpu_usage_ros2.log  #不定な値（cpu使用率）は何をテストすればいいか分からない
