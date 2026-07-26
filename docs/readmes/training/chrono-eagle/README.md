<!-- source: https://github.com/MingziFu9/chrono-eagle.git sha: 809dfe1706deee5a26b00948e989baf1bce2a476 readme: master/README.md -->
# MingziFu9/chrono-eagle

Cloud-based Python Training Platform with Docker isolation, VS Code Server IDE & AI Assistant

---

<div align="center">

# 🦅 Chrono-Eagle

**云端 Python 实训平台 | Cloud-based Python Training Platform**

基于 Docker 容器隔离 + VS Code Server + AI 智能助手的多用户编程实训环境

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-Compose-2496ED?logo=docker)](docker-compose.yml)
[![Node.js](https://img.shields.io/badge/Node.js-18+-339933?logo=node.js)](backend/)
[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](docker/code-server/)

</div>

---

## ✨ 核心特性

| 特性 | 描述 |
|---|---|
| 🚀 **零配置启动** | 学生通过浏览器即可使用完整的 VS Code IDE 环境 |
| 🔒 **完全隔离** | 每个学生独立 Docker 容器（一人一舱），互不干扰 |
| 🤖 **AI 赋能** | 集成 vLLM / Ollama 大模型，提供实时代码诊断与学习指导 |
| 📊 **学习追踪** | 实验进度、AI 交互次数、学习时长等数据全程记录 |
| 🎓 **教学友好** | 支持入门/中级/高级三级难度实验模板，教师可自定义 |
| 🛡️ **安全沙盒** | CPU/内存/磁盘资源限制 + 网络隔离 + 自动清理 |
| 📈 **弹性扩展** | 容器按需创建/销毁，支持数十到数百并发用户 |

## 🏗️ 系统架构

<div align="center">
<img src="docs/ce_network_topology.svg" alt="网络拓扑结构" width="900"/>
</div>

### 技术栈

```
┌─────────────────────────────────────────────────────┐
│  前端层        Nginx + 原生 HTML/CSS/JS              │
├─────────────────────────────────────────────────────┤
│  网关层        Traefik v2.10 (反向代理 + 动态发现)    │
├─────────────────────────────────────────────────────┤
│  应用层        Node.js 18 / Express (API Server)     │
│               ├─ containerManager (dockerode)        │
│               ├─ aiAssistant (OpenAI-compatible)     │
│               └─ authMiddleware (JWT)                │
├─────────────────────────────────────────────────────┤
│  数据层        PostgreSQL 15 + Redis 7               │
├─────────────────────────────────────────────────────┤
│  容器层        Docker (code-server + Python 3.11)    │
│               Streamlit / Gradio 可视化渲染           │
├─────────────────────────────────────────────────────┤
│  AI 层         vLLM + Qwen3 (OpenAI-compatible API) │
└─────────────────────────────────────────────────────┘
```

## 🚀 快速开始

### 前置条件

- **Docker** >= 20.10 & **Docker Compose** >= 2.0
- **服务器** 推荐 4 核 8G 以上（每个学生容器约 512MB）
- **AI 服务**（可选）: vLLM / Ollama 部署的大语言模型

### 1. 克隆仓库

```bash
git clone https://github.com/YOUR_USERNAME/chrono-eagle.git
cd chrono-eagle
```

### 2. 配置环境变量

```bash
cp .env.example .env
# 编辑 .env，设置数据库密码、JWT 密钥和 AI 模型端点
vim .env
```

### 3. 构建学生容器镜像

```bash
cd docker/code-server
docker build -t python-lab-codeserver:latest .
cd ../..
```

### 4. 启动所有服务

```bash
docker-compose up -d
```

### 5. 验证部署

```bash
# 检查服务状态
docker-compose ps

# 访问平台
# 主页: http://your-server:9080
# 管理后台: http://your-server:9080/admin.html
# Traefik Dashboard: http://your-server:8888
```

**默认管理员账号**: `admin` / `admin123`（⚠️ 首次登录请立即修改）

## 📁 项目结构

```
chrono-eagle/
├── backend/                    # 后端 API 服务
│   ├── server.js              # Express 主入口 (649行)
│   ├── services/
│   │   ├── containerManager.js # Docker 容器生命周期管理
│   │   └── aiAssistant.js     # AI 助手（OpenAI 兼容接口）
│   ├── routes/
│   │   └── lab.js             # 实验相关 API 路由
│   ├── middleware/
│   │   └── authMiddleware.js  # JWT 认证中间件
│   ├── Dockerfile
│   └── package.json
├── frontend/                   # 前端页面
│   ├── index.html             # 系统首页 / 状态面板
│   ├── login.html             # 登录页
│   ├── register.html          # 注册页
│   ├── dashboard.html/js      # 学生实验室仪表板
│   ├── ide.html               # VS Code IDE 集成页
│   ├── experiment.html        # 实验详情页
│   ├── admin.html/js          # 管理后台
│   ├── nginx.conf             # Nginx 配置
│   └── Dockerfile
├── database/
│   ├── schema.sql             # 数据库建表脚本 (6表+2视图)
│   └── add_progress_table.sql # 学习进度表
├── docker/
│   ├── code-server/           # 学生容器镜像
│   │   ├── Dockerfile         # Python 3.11 + code-server 4.20
│   │   ├── requirements.txt   # Python 依赖
│   │   └── extensions.txt     # VS Code 扩展列表
│   ├── python-lab/            # 轻量 Python 环境
│   │   └── Dockerfile
│   └── traefik/               # 反向代理配置
│       ├── traefik.yml        # Traefik 静态配置
│       └── dynamic-config.yml # 动态路由 + 中间件
├── docs/                       # 文档与架构图
│   └── ce_network_topology.svg
├── docker-compose.yml          # 服务编排
├── insert_experiments.sql      # 示例实验数据
├── DEPLOYMENT.md               # 详细部署文档
├── .env.example                # 环境变量模板
├── .gitignore
├── LICENSE                     # MIT License
└── README.md
```

## 📊 数据库设计

| 表名 | 用途 |
|---|---|
| `users` | 用户管理（学生/教师/管理员） |
| `experiments` | 实验模板（标题/描述/难度/初始代码） |
| `lab_sessions` | 实验会话（容器状态/活动时间） |
| `container_metadata` | 容器配置（端口/资源限制） |
| `ai_interactions` | AI 助手交互记录（审计与分析） |
| `learning_progress` | 学习进度追踪（成绩/尝试次数） |

## 🤖 AI 助手配置

系统支持任何 **OpenAI-compatible API** 作为 AI 后端：

| 方案 | 配置示例 |
|---|---|
| **vLLM** (推荐) | `OLLAMA_HOST=http://gpu-server:8000/v1` |
| **Ollama** | `OLLAMA_HOST=http://localhost:11434/v1` |
| **OpenAI** | `OLLAMA_HOST=https://api.openai.com/v1` |

## 🔐 安全特性

- **容器沙盒**: 每个学生独立容器，CPU 1核 / 内存 512MB / 磁盘 5GB
- **JWT 认证**: 基于 JSON Web Token 的用户认证
- **密码加密**: bcrypt 哈希存储
- **速率限制**: Traefik 内置请求频率控制
- **网络隔离**: Docker bridge 网络隔离
- **自动清理**: 空闲容器自动回收

## 📝 License

[MIT](LICENSE) © 2026 ChronoEagle Contributors

---

<div align="center">
<sub>Built with ❤️ for education</sub>
</div>
