#!/usr/bin/python3
# SPDX-FileCopyrightText: 2024 Yuuki Ishizaka
# SPDX-License-Identifier: BSD-3-Clause

import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class Talker(Node):  # Nodeクラスを継承したTalkerクラス
    def __init__(self):  # 初期化メソッド
        super().__init__("talker")  # ノード名を"talker"として初期化
        self.pub = self.create_publisher(Float32, "sensor_data", 10)  # トピック"sensor_data"を作成
        self.create_timer(1.0, self.publish_temperature)  # 1秒ごとにpublish_temperatureを呼び出し

    def publish_temperature(self):  # コールバックメソッド
        msg = Float32()
        msg.data = random.uniform(20.0, 30.0)  # ランダムな温度データを生成
        self.pub.publish(msg)  # トピックにデータを送信
        self.get_logger().info("Published temperature")  # ログに最低限の情報を表示

def main():  # エントリーポイント
    rclpy.init()
    node = Talker()  # Talkerのオブジェクトを作成
    rclpy.spin(node)  # ノードのスピンを開始
    node.destroy_node()  # ノード終了時にリソースを解放
    rclpy.shutdown()  # ROS 2のシャットダウン

if __name__ == "__main__":
    main()
