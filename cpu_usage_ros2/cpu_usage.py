import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import psutil


class Talker(Node):
    def __init__(self):
        super().__init__("talker")
        self.pub = self.create_publisher(Float32, "cpu_usage", 10)
        self.create_timer(0.5, self.cb)
        self.cpu_usage = psutil.cpu_percent(interval=1)


    def cb(self):
        msg = ()
        msg.data = self.cpu_usage
        self.pub.publish(msg)


def main():
    rclpy.init()
    node = Talker()
    rclpy.spin(node)
