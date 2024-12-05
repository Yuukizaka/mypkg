import rclpy
from rclpy.node import Node
from std_msgs.msg import Int16

class Talker(Node):  # "Listener" ではなく "Talker" と命名
    def __init__(self):  # コンストラクタ名を修正
        super().__init__("talker")  # ノード名を指定
        self.pub = self.create_publisher(Int16, "countup", 10)
        self.create_timer(0.5, self.cb)
        self.n = 0

    def cb(self):  # コールバックメソッド
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.get_logger().info(f"listener: {msg.data}")
        self.n += 1

def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()  # ノードのクリーンアップ
    rclpy.shutdown()

