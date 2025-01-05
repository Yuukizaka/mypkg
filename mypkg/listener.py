import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32

class Listener(Node):  # クラス名を "Listener" に修正
    def __init__(self):
        super().__init__("listener")  # ノード名を "listener" として初期化
        self.sub = self.create_subscription(
            Float32, "sensor_data", self.callback, 10)  # トピック "sensor_data" を購読
        self.get_logger().info("Sensor Listener Node is running.")

    def callback(self, msg):  # コールバックメソッド
        # トピックから受信したデータを表示
        self.get_logger().info(f"Received temperature: {msg.data:.2f} °C")

def main():
    rclpy.init()
    node = Listener()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


