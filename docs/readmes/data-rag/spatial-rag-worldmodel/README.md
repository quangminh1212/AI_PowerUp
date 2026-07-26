<!-- source: https://github.com/AdnanSattar/Spatial-RAG-Worldmodel.git sha: 6e8597dd7dd62f2fc1a457e798638b4214d6d729 readme: main/README.md -->
# AdnanSattar/Spatial-RAG-Worldmodel

A Spatial Retrieval-Augmented Generation system for latent world models, designed for embodied spatial intelligence in robotics, autonomous navigation, and embodied AI. Features ROS2 integration, real-time inference @ 25Hz, and complete robot build guide.

---

# Spatial-RAG World Model

A **Spatial Retrieval-Augmented Generation** system for latent world models, designed for embodied spatial intelligence in robotics, autonomous navigation, and embodied AI.

<p align="center">
  <img src="docs/images/front-end.png" alt="Spatial-RAG Dashboard" width="800"/>
</p>

## 🎯 What is Spatial-RAG?

This project implements a memory-augmented latent world model that:

- **Encodes** observations (RGB, depth, proprioception) into compact latent representations
- **Stores** latent states with spatial metadata in a vector database
- **Retrieves** relevant past experiences using hybrid spatial + latent similarity search
- **Predicts** future states by conditioning on retrieved memory context

**Result:** Improved prediction accuracy (15-30%) and sample efficiency for embodied agents.

> 📖 **New to Spatial-RAG?** See the [Practical Usage Guide](docs/PRACTICAL_GUIDE.md) for real-world applications and examples.

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         SPATIAL-RAG SYSTEM OVERVIEW                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│   PERCEPTION           WORLD MODEL                    MEMORY                 │
│   ──────────           ───────────                   ────────                │
│                                                                              │
│   📷 Camera  ──────►  ┌─────────┐                 ┌──────────┐              │
│                       │ Encoder │ ──► z[32] ─────►│  Qdrant  │              │
│   🎮 Actions ──────►  └────┬────┘        │        │ (Vector  │              │
│                            │             │        │   DB)    │              │
│   📍 Pose    ──────►       ▼             │        └────┬─────┘              │
│                       ┌──────────┐       │             │                    │
│                       │Transition│◄──────┴─────────────┘                    │
│                       └────┬─────┘     Retrieved                            │
│                            │           Memories                             │
│                            ▼                                                 │
│                       ┌─────────┐                                           │
│                       │ Decoder │ ──► 🖼️ Predicted Frame                    │
│                       └─────────┘                                           │
│                            │                                                 │
│                            ▼                                                 │
│                       ┌─────────┐                                           │
│                       │ Policy  │ ──► 🤖 Motor Commands                     │
│                       └─────────┘                                           │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key Components:**
```
Perception → Encoder → Latent z → Memory Bank (Qdrant)
                          ↓              ↓
                   Transition ← ← Retrieval Module
                          ↓
                   Decoder → Reconstruction
                          ↓
                   Policy/Planner → Actions
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <repo-url>
cd Spatial-RAG-Worldmodel

# Install dependencies (optional for local dev)
pip install -r requirements.txt
```

### 2. Docker Setup (Recommended)

```bash
# Build the shared base image
docker compose build base

# Start core services (Qdrant + API)
docker compose --profile core up -d

# Start UI dashboard
docker compose --profile ui up -d
```

<p align="center">
  <img src="docs/images/docker.png" alt="Docker Services Running" width="700"/>
</p>

**Access:**
- 🌐 **API**: http://localhost:8080
- 📚 **API Docs**: http://localhost:8080/docs
- 🖥️ **UI Dashboard**: http://localhost:3000
- 🔍 **Qdrant**: http://localhost:6333

<p align="center">
  <img src="docs/images/api.png" alt="FastAPI Swagger Docs" width="700"/>
</p>

### 3. Generate Data & Train

```bash
# Generate synthetic data
docker compose run --rm generate-data python scripts/simulate_env.py --out data/trajectories --n 500

# Train models
docker compose run --rm train

# Restart API with trained model
docker compose restart api
```

### 4. Test in UI

1. Open http://localhost:3000
2. Click "Generate Random Latent"
3. Click "Start Rollout"
4. Watch predicted frames stream in real-time!

## 🤖 Real-World Applications

| Application | Use Case |
|-------------|----------|
| 🚁 **Autonomous Drones** | Navigate cities using past flight memories |
| 🚗 **Self-Driving Cars** | Predict pedestrian behavior at intersections |
| 📦 **Warehouse Robots** | Remember item locations for faster picking |
| 🏠 **Home Assistants** | Learn house layout, remember where things are |
| 👓 **AR Navigation** | Predictive overlays based on spatial memory |

> 📖 See [Practical Usage Guide](docs/PRACTICAL_GUIDE.md) for detailed examples.

## 🐳 Docker Services

All services share optimized images (~25GB total):

| Service | Purpose |
|---------|---------|
| `api` | FastAPI inference server |
| `ui` | Next.js dashboard |
| `qdrant` | Vector database |
| `train` | Model training |
| `ros2` | ROS2 robotics node |
| `generate-data` | Synthetic data |
| `collect` | Data collection |

### Common Commands

```bash
# Start services
docker compose --profile core up -d           # API + Qdrant
docker compose --profile ui up -d             # Dashboard
docker compose --profile ros2 up -d           # ROS2 node

# Run tasks
docker compose run --rm train                 # Train model
docker compose run --rm experiment            # Run experiments
docker compose run --rm reports               # Generate reports

# Manage
docker compose logs -f api                    # View logs
docker compose ps                             # Check status
docker compose down                           # Stop all
```

## 🤖 ROS2 Integration

Real-time robotics integration with ROS2 Humble. **✅ Fully tested and working!**

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ROS2 DATA FLOW (@25Hz)                               │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                              │
│  📷 Camera ───► webcam_bridge.py ───► FastAPI ───► ROS2 Bridge             │
│                      │                   │              │                   │
│                   Capture             Encode         Publish                │
│                   Frames            to z[32]        Topics                  │
│                                         │              │                    │
│                                         ▼              ▼                    │
│                                    ┌─────────┐   ┌──────────┐              │
│                                    │ z_next  │   │ /latent  │              │
│                                    │predicted│   │/latent_  │              │
│                                    └─────────┘   │  next    │              │
│                                                  └────┬─────┘              │
│                                                       │                     │
│  🎮 /actions ◄───────────────────────────────────────┘                     │
│       │                                                                     │
│       ▼                                                                     │
│  🤖 Motors                                                                  │
│                                                                              │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Quick Start

```bash
# Start all ROS2 services
docker compose --profile ros2 up -d

# Stream webcam with predictions to ROS2 (on Windows host)
python scripts/webcam_bridge.py --mode api --camera 0 --fps 5 --display --ros2-bridge http://localhost:8082
```

### Topics

| Topic | Direction | Rate | Description |
|-------|-----------|------|-------------|
| `/latent` | Publish | ~25Hz | Current 32-dim latent state |
| `/latent_next` | Publish | ~25Hz | Predicted next latent |
| `/actions` | Subscribe | 5Hz+ | Action commands [x, y] |
| `/camera/image_raw` | Subscribe | - | Camera images |

### Send Action Commands

```bash
# Publish actions (forward motion)
docker compose exec ros2-bridge bash -c "source /opt/ros/humble/setup.bash && \
  ros2 topic pub /actions std_msgs/Float32MultiArray '{data: [1.0, 0.5]}' --rate 5"
```

### Monitor Topics

```bash
# Echo latent vector
docker compose exec ros2-bridge bash -c "source /opt/ros/humble/setup.bash && ros2 topic echo /latent --once"

# Echo prediction
docker compose exec ros2-bridge bash -c "source /opt/ros/humble/setup.bash && ros2 topic echo /latent_next --once"

# Check rates (~25Hz)
docker compose exec ros2-bridge bash -c "source /opt/ros/humble/setup.bash && ros2 topic hz /latent"
```

## 📷 Webcam Streaming (Windows)

Stream your laptop webcam to the API for real-time encoding:

```powershell
# Install on Windows (NOT Docker)
pip install opencv-python requests pillow

# List cameras
python scripts/webcam_bridge.py --mode list

# Stream with live preview
python scripts/webcam_bridge.py --mode api --camera 0 --display
```

Output:
```
Streaming to http://localhost:8080 at 5 FPS
Frame 100: latent mean=-0.0575, FPS=4.8
```

> 📖 See [Webcam Streaming Guide](docs/WEBCAM_STREAMING.md) for details.

## 📊 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/encode` | POST | Image → latent |
| `/webcam/encode` | POST | Base64 image → latent (for webcam) |
| `/predict` | POST | One-step prediction |
| `/rollout` | POST | Multi-step rollout |
| `/stream-rollout` | GET | SSE streaming |
| `/retrieve` | POST | Memory search |

## 📈 Results

| Model | Latent MSE | Improvement |
|-------|------------|-------------|
| Baseline | 0.0234 | - |
| **Spatial-RAG** | 0.0198 | **15.4%** |

## 🚀 Roadmap: Full Autonomy

| Feature | Status | Description |
|---------|--------|-------------|
| ✅ Latent Encoding | Done | Real-time camera → 32-dim latent @ 25Hz |
| ✅ Next-State Prediction | Done | `/latent_next` predictions |
| ✅ Memory Retrieval | Done | Qdrant-based spatial memory |
| ✅ ROS2 Integration | Done | `/latent`, `/actions` topics |
| 🔜 Policy Network | Planned | Neural net: latent → motor commands |
| 🔜 Robot Training Data | Planned | Collect from YOUR robot |
| 🔜 Path Planning | Planned | A*/RRT goal navigation |

> 📖 See [Robot Integration Guide](docs/ROBOT_INTEGRATION.md) for full autonomy details.

### Recommended Hardware

| Option | Price (PKR) | Inference | Best For |
|--------|-------------|-----------|----------|
| **Pi 4 (4GB)** | ~Rs 18,000 | ~50ms | Budget robots |
| **Pi 5 (8GB)** | ~Rs 28,000 | ~30ms | Faster autonomy |
| **Jetson Orin** | ~Rs 60,000+ | ~5ms | Production |

> ❌ Pi Zero not recommended (too slow for real-time inference)

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [📖 Practical Guide](docs/PRACTICAL_GUIDE.md) | Real-world applications and examples |
| [🤖 Robot Integration](docs/ROBOT_INTEGRATION.md) | End-to-end robot setup guide |
| [🛠️ Build Guide](docs/BUILD_GUIDE.md) | **Shopping list + assembly instructions** |
| [📷 Webcam Streaming](docs/WEBCAM_STREAMING.md) | Stream laptop camera to API |
| [🏗️ Design](DESIGN.md) | Architecture and system design |
| [🚀 Deployment](DEPLOYMENT.md) | Production deployment guide |
| [📷 Data Collection](docs/DATA_COLLECTION.md) | Collecting robot data |
| [📋 Quick Reference](docs/QUICK_REFERENCE.md) | Command cheat sheet |

## 📁 Project Structure

```
Spatial-RAG-Worldmodel/
├── api/                    # FastAPI server
├── ui/                     # Next.js dashboard
├── ros2_ws/                # ROS2 integration
├── src/                    # Core library
│   ├── models/             # Encoder, Transition, Decoder
│   ├── memory/             # Qdrant, Faiss stores
│   └── datasets/           # Data loading
├── scripts/                # Training, export, collection
├── docs/                   # Documentation
└── docker-compose.yml      # Service orchestration
```

## ⚙️ Configuration

| Variable | Default | Description |
|----------|---------|-------------|
| `Z_DIM` | 32 | Latent dimension |
| `ACTION_DIM` | 2 | Action dimension |
| `TOPK` | 8 | Retrieved memories |
| `QDRANT_HOST` | localhost | Qdrant host |

## 📄 License

MIT License

## 📝 Citation

```bibtex
@software{spatial_rag_worldmodel,
  title={Spatial-RAG World Model for Embodied Spatial Intelligence},
  author={Adnan Sattar},
  year={2025},
  url={https://github.com/adnansattar/Spatial-RAG-Worldmodel}
}
```

## 📚 References

- [Spatial Retrieval Augmented Generation](https://arxiv.org/abs/2502.18470)
- [DreamerV3: World Models](https://arxiv.org/abs/2301.04104)
- [H3: Uber's Spatial Index](https://h3geo.org/)
