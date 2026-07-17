from rclpy.lifecycle import LifecycleNode

from agx_arm_ctrl.agx_arm_ctrl_single_node import AgxArmRosNode


def test_arm_driver_is_lifecycle_managed():
    assert issubclass(AgxArmRosNode, LifecycleNode)
