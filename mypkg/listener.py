#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Yuuki Ishizaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
from decimal import Decimal, ROUND_HALF_UP


class Listener(Node):
    def __init__(self):
        super().__init__("listener")
        self.sub = self.create_subscription(
            Float32, "sensor_data", self.callback, 10)
        self.get_logger().info("Sensor Listener Node is running.")

    def callback(self, msg):
        formatted_data = Decimal(msg.data).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        self.get_logger().info(f"Received temperature: {formatted_data} °C")


def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()

