import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):

    def __init__(self):
        super().__init__("pub_node_test")
        self.counter_ = 0
        # create_publisher needs 3 parameters: Msg Type, message, and buffer size
        self.publisher = self.create_publisher(String, "Hello_Justin", 10)
        self._timer = self.create_timer(0.5, self.publish_hello)
        self.get_logger().info("publishing message has started")

    def publish_hello(self):
        msg = String()
        self.counter_ += 1
        msg.data = "Hello Justin " + str(self.counter_)
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()