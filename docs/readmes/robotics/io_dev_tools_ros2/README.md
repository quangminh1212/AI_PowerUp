<!-- source: https://github.com/ioai-tech/io_dev_tools_ros2.git sha: c8549cf46b7f02321d26a6bcdd7956f9439c383e readme: master/README.md -->
# ioai-tech/io_dev_tools_ros2

ROS 2 developer tooling for IO-AI embodied data workflows

---

# io_dev_tools_ros2



## Getting started

Make workspace
```
mkdir -p ~/ws_io_dev/src
cd ws_io_dev/src
```
Get code from gitlab
```
git clone http://git.io-intelligence.com/io/io_dev_tools_ros2
```
Get code from github
```
git clone https://github.com/ioai-tech/io_dev_tools_ros2.git
```
Build
```
cd ~/ws_io_dev/
colcon build --packages-select <ros_pakages>
```
For usage instructions for each package, please refer to the respective package's README.