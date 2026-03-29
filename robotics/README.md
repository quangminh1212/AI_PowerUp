# 🤖 Robotics & Embodied AI

Simulation environments, navigation, reinforcement learning, and physical AI.

## Overview

This directory contains 10 submodules for training and deploying AI agents in physical and simulated environments — from photorealistic 3D simulators to robot control frameworks and RL environments.

## Submodules (10)

### 3D Simulation
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`habitat-sim`](https://github.com/facebookresearch/habitat-sim) | Meta | Photorealistic 3D simulator for embodied AI |
| [`habitat-lab`](https://github.com/facebookresearch/habitat-lab) | Meta | Embodied AI research platform |
| [`isaaclab`](https://github.com/isaac-sim/IsaacLab) | NVIDIA | Robot learning framework on Isaac Sim |
| [`mujoco`](https://github.com/google-deepmind/mujoco) | DeepMind | Physics engine for robotics research |

### Reinforcement Learning
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`gymnasium`](https://github.com/Farama-Foundation/Gymnasium) | Farama | Standard RL environment API |
| [`robosuite`](https://github.com/ARISE-Initiative/robosuite) | Stanford | Robot manipulation simulation |
| [`pybullet`](https://github.com/bulletphysics/bullet3) | Bullet | Real-time physics simulation |

### Robot Operating System
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`ros2`](https://github.com/ros2/ros2) | ROS | Robot Operating System 2 |
| [`nav2`](https://github.com/ros-navigation/navigation2) | ROS | Autonomous navigation framework |

### Datasets & Research
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`openx`](https://github.com/google-deepmind/open_x_embodiment) | DeepMind | Open X-Embodiment robot dataset |

## Usage

```bash
git submodule update --init --depth 1 robotics/gymnasium
git submodule update --init --depth 1 robotics/mujoco
```
