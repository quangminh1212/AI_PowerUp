# 🤖 Robotics & Embodied AI

Simulation environments, physics engines, and platforms for training robots and embodied AI agents.

## Overview

This directory contains **10 submodules** covering the full robotics AI stack — from physics simulators (MuJoCo, PyBullet, Isaac Lab) to navigation systems (Nav2, ROS2), benchmarks (Habitat, Gymnasium), and datasets (Open X-Embodiment).

## Submodules (10)

### Physics Simulators
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`mujoco`](https://github.com/google-deepmind/mujoco) | DeepMind | Multi-joint dynamics simulator for robotics research |
| [`pybullet`](https://github.com/bulletphysics/bullet3) | Bullet | Real-time collision detection and physics simulation |
| [`isaaclab`](https://github.com/isaac-sim/IsaacLab) | NVIDIA | GPU-accelerated robot learning framework |

### Environment & Benchmark
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`gymnasium`](https://github.com/Farama-Foundation/Gymnasium) | Farama | Standard RL environment API (successor to OpenAI Gym) |
| [`habitat-sim`](https://github.com/facebookresearch/habitat-sim) | Meta | Fast 3D simulator for embodied AI |
| [`habitat-lab`](https://github.com/facebookresearch/habitat-lab) | Meta | Embodied AI task and benchmark framework |
| [`robosuite`](https://github.com/ARISE-Initiative/robosuite) | ARISE | Robotic manipulation simulation benchmark |

### Robot Operating Systems
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`ros2`](https://github.com/ros2/ros2) | Open Robotics | Robot Operating System 2 |
| [`nav2`](https://github.com/ros-navigation/navigation2) | ROS | Navigation stack for mobile robots |

### Datasets
| Submodule | Source | Description |
|-----------|--------|-------------|
| [`openx`](https://github.com/google-deepmind/open_x_embodiment) | DeepMind | Open X-Embodiment robotic manipulation dataset |

## Key Capabilities

| Capability | Best Options |
|-----------|--------|
| **Physics Simulation** | mujoco, pybullet, isaaclab |
| **RL Training** | gymnasium, robosuite |
| **3D Navigation** | habitat-sim, habitat-lab |
| **Production Robots** | ros2, nav2 |
| **Datasets** | openx |

## Usage

```bash
# Init MuJoCo physics engine
git submodule update --init --depth 1 robotics/mujoco
pip install mujoco

# Setup Gymnasium for RL
git submodule update --init --depth 1 robotics/gymnasium
pip install gymnasium
```
