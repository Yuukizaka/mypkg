#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuuki Ishizaka
# SPDX-License-Identifier: BSD-3-Clausea

WS_DIR=~/ros2_ws
LOG_FILE="/tmp/mypkg.log"

# Build the package
cd $WS_DIR
source /opt/ros/humble/setup.bash
colcon build
source $WS_DIR/install/setup.bash

# Run test
echo "Running talk_listen.launch.py..."
timeout 10 ros2 launch mypkg talk_listen.launch.py | tee -a $LOG_FILE

# Check if listener received sensor data
if grep -q "Received temperature" "$LOG_FILE"; then
    echo "Test passed!"
    exit 0
else
    echo "Test failed: 'Received temperature' not found in logs."
    exit 1
fi
