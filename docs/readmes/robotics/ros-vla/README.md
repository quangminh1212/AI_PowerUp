<!-- source: https://github.com/jonasdieker/ros-vla.git sha: f8ce13a1d3a7ad93789289d7423f5b6f6702630e readme: main/README.md -->
# jonasdieker/ros-vla

End-to-end Embodied AI Sim2Real Pipeline

---

# ROS VLA

## Getting Started

Open in VS Code devcontainer: `Ctrl + Shift + P` type `Dev Container: ...`

### ROS2 + Sim run:
```bash
# In terminal 1, run the Gazebo simulation
ros2 launch lerobot_description so101_gazebo.launch.py

# In terminal 2, load the ros2 controllers and run MoveIt
ros2 launch lerobot_controller so101_controller.launch.py && \
  ros2 launch lerobot_moveit so101_moveit.launch.py
```

### VLA:
This pkg needs numpy 2.0, but ROS2 is using 1.0. To separate the dependencies, we use venv + uv.

However, the installation of the dependencies is already part of the Docker image, you just have to install the pkg itself:

```bash
# In terminal 3, run VLA
cd /home/ubuntu/ros_ws/src/lerobot_robot_ros
source ../../.venv/bin/activate
uv pip install -e .
python scripts/run_policy.py
```

## Simple Sim Environment for Inference/Training
![sim-env](assets/sim_env_example.png)

In addition to the SO101 robot, the description also includes two camera. One attached to the arm `wrist_camera` and one mounted above the scene facing down `scene_camera`.

## To Do

- [x] Get description + controllers to work
- [x] Get Gazebo + MoveIt
- [x] Dockerize for easy usage
- [x] Simulate cameras (wrist and scene)
- [x] Create world with task e.g. red ball + more realistic background e.g. room.
- [x] Run lerobot as is (no fine-tuning)
- [x] Dataset Recorder
- [ ] Fine-tuning
- [ ] (optional) Foxglove integration?
- [ ] If it work without fine-tuning -> long horizon tasks
    - Orchestrator/planner agent to break down longer task into smaller ones
- [ ] Isaac Sim
- [ ] Try with different robot e.g. mobile robot