<!-- source: https://github.com/meta-tabchen/pixelflow.git sha: 614898234a1ee580217b89ae0826493f4ca41ca3 readme: main/README.md -->
# meta-tabchen/pixelflow

PixelFlow is a professional-grade AI visual creation engine that reimagines image generation through a node-based workflow. Designed for concept artists, designers, and prompt engineers, it leverages the power of Gemini 3 and Imagen models to turn complex ideas into structured, repeatable creative pipelines.

---


# PixelFlow v2.0 🎨⚡

> **Visual Logic Without Boundaries.**

**PixelFlow** is a professional-grade AI visual creation engine that reimagines image generation through a node-based workflow. Designed for concept artists, designers, and prompt engineers, it leverages the power of Google's **Gemini 2.5 Flash** and **Gemini 3 Pro** models to turn complex ideas into structured, repeatable creative pipelines.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![React](https://img.shields.io/badge/React-19-61dafb.svg)
![Status](https://img.shields.io/badge/Status-v2.0_Ready-green.svg)

---

## ✨ Key Features

### ♾️ Infinite Canvas Architecture
Break free from linear chat interfaces. Build complex logic chains where data flows visually from one node to another.
- **Topological Execution:** Run entire node groups in sequence.
- **Reference Chaining:** Use the output of one generation as the reference input for the next (Image-to-Image).
- **Group & Organize:** Cluster nodes into logical groups to keep your workspace clean.

### 🎥 Camera Director
The industry-first **Camera Director** panel gives you cinematic control over your generations without needing to know technical photography terms.
- **Framing:** Extreme Wide Shot, Full Body, Close-Up, Macro.
- **Angles:** High Angle, Low Angle, Overhead, Dutch Tilt.
- **Motion:** Pan, Dolly Zoom, Handheld, FPV Drone.

### ⚡ Smart Productivity Tools
- **Slash Commands (`/`):** Instantly inject professional presets like "Cyberpunk", "Photorealism", or "Studio Lighting" directly into your prompt.
- **Magic Optimize (`Ctrl+1`):** Stuck on a prompt? Let the AI rewrite your simple concept into a highly detailed, artistic description.
- **Workflow Library:** Save your best node graphs as reusable templates. Share logic between projects.

### 💾 Robust Data Management
- **Auto-Save:** Your workspace is automatically saved to local storage.
- **History Gallery:** Every image generated is archived with full metadata (prompt, model, seed, camera settings).
- **Vision Analysis:** Drag an image into the canvas to have Gemini analyze and describe it for you.

---

## 🚀 Tech Stack

- **Frontend:** React 19, TypeScript, Tailwind CSS
- **Canvas Engine:** ReactFlow 11
- **AI Integration:** Google GenAI SDK (Gemini 2.5 Flash Image, Gemini 3 Pro Image)
- **Image Processing:** Fabric.js (In-canvas annotation)
- **Storage:** IndexedDB (via idb-keyval)
- **Icons:** Lucide React

---

## 🛠️ Getting Started

### Prerequisites
You will need a Google Gemini API Key. Get one at [AI Studio](https://aistudio.google.com/).

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pixelflow.git
   cd pixelflow
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Configure your environment variables:
   Create a `.env` file in the root directory:
   ```env
   API_KEY=your_gemini_api_key_here
   ```
   *Note: Users can also enter their own API key via the Settings UI.*

4. Start the development server:
   ```bash
   npm run dev
   ```

---

## 📖 Usage Guide

1. **Dashboard:** Start here to manage multiple projects or view your gallery.
2. **Workspace:**
   - **Right Click / Sidebar:** Add `Generator`, `Text`, or `Image` nodes.
   - **Connect:** Drag cables between nodes to define the flow.
   - **Camera:** Click the camera icon on a Generator node to set the scene.
   - **Run:** Execute individual nodes or entire groups.
3. **Editor:** Click the pencil icon on any generated result to annotate or paint over it before using it as a reference for the next step.

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- Built for the next generation of AI creators.
- Powered by Google Gemini.
- Inspired by node-based tools like ComfyUI and Blender.

---

Developed with ❤️ by the **PixelFlow Team**.
