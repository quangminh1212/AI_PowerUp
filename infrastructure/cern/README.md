# Cern: A Customer Service AI Assistant

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Project Blueprint](https://img.shields.io/badge/Project-Blueprint-blueviolet)](#an-open-source-blueprint-for-your-custom-ai-assistant)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)](https://github.com/Aeshp/Cern_app)
[![Deployment](https://img.shields.io/badge/deployment-Hugging%20Face-blue)](https://huggingface.co/spaces)
[![Live Site](https://img.shields.io/badge/Live-Demo-brightgreen)](https://cernofregime.netlify.app/)
[![Training Code](https://img.shields.io/badge/Training%20Code-GitHub-yellow)](https://github.com/Aeshp/deepseekR1finetune)
[![Model Card](https://img.shields.io/badge/Model-Hugging%20Face-orange)](https://huggingface.co/Aeshp/deepseekR1tunedchat)


This repository contains the source code for **Cern**, a complete, full-stack AI assistant. The project is built with a modern 3-tier architecture, simulating a human customer service specialist for the fictional company, **Regime Audio**.

More importantly, this repository serves as a **production-ready, open-source boilerplate** for building your own custom AI assistants.

---
![Cern application](./assets/Cern.png)

## An Open-Source Blueprint for Your Custom AI Assistant

This repository is not just a demo; it is an **MIT-licensed, full-stack blueprint** designed for you to build and deploy your own commercial or personal AI assistants.

The `Cern` assistant is just one example of what you can build. You are encouraged to take this codebase and:

* **Train Your Own AI:** Use the [Fine-Tuning Repository](https://github.com/Aeshp/deepseekR1finetune) to train your model on a custom dataset, starting from either the **base model** or the **provided fine-tuned checkpoint**.
* **Rebrand the Frontend:** Modify the React application with your own branding, UI, and features.
* **Own Your Data:** Connect your own MongoDB Atlas cluster to store all conversation data.
* **Add Telemetry:** Integrate your own analytics and monitoring tools into the Node.js backend.

This entire 3-tier architecture serves as a complete, scalable starting point for your custom AI projects.

---

## The AI Model: From Generalist to Specialist

The core of this project is a bespoke language model, fine-tuned to perform a specialized role. The training process involved two key stages:

1.  **Base Model Training:** The model began as a powerful, general-purpose model, pre-trained on a vast and diverse dataset. This gave it a broad understanding of language, context, and reasoning.
2.  **Specialized Fine-Tuning:** It was then meticulously fine-tuned using a custom dataset built for the **Regime Audio** company (this was a test case). This second stage imbued the model with a specific persona, knowledge base, and conversational rules.

* **Hugging Face Model Card:** [**Aeshp/deepseekR1tunedchat**](https://huggingface.co/Aeshp/deepseekR1tunedchat)
* **Fine-Tuning Repository:** [**Aeshp/deepseekR1finetune**](https://github.com/Aeshp/deepseekR1finetune.git).

---
## Live Demo

Try the live, deployed version of **Cern** here:
https://cernofregime.netlify.app/

> Note: This site is deployed on Netlify. If you run into issues with the demo (broken UI, missing features, etc.), please check that your local `.env` is configured to point to the correct backend URL, clear your browser cache, or open an issue on the repo: https://github.com/Aeshp/Cern/issues

## Project Structure

This project uses a 3-tier architecture, organized as follows:

* `frontend/`: The React UI. This is the only part the user interacts with. It only communicates with the `Backend`.
* `Backend/`: The Node.js logic server. It uses Express to handle API requests, Mongoose to connect to MongoDB for storing chat history, and manages user sessions. It calls the `HF_Backend` to get AI responses.
* `HF_Backend/`: The Python AI inference server. It uses FastAPI to serve the quantized language model on a GPU. Its only job is to generate text.

---

## Running the Application Locally

To run the full application, you will need to run the **`Backend`** (Node.js) and the **`frontend`** (React) servers. The `HF_Backend` is designed to run on a separate, dedicated service (like Hugging Face Spaces) as it requires a GPU.

### Prerequisites

* Git
* Node.js (v14 or later) & npm
* A **MongoDB Atlas Account** (for the free cluster) and your **MongoDB URI** connection string.
* A deployed instance of the `HF_Backend` (e.g., on [Hugging Face Spaces](https://huggingface.co/spaces)) and its **public URL**.

---

### Step 1: Run the Logic Backend (Node.js)

First, get the Node.js server running. This server connects to your database and the live AI model.

1.  **Navigate to the `Backend` directory:**
    ```sh
    cd Backend
    ```

2.  **Create an `.env` file:**
    Create a file named `.env` in the `Backend` directory and add your secret keys. It must include:
    ```.env
    # Your MongoDB Atlas connection string
    MONGODB_URI="mongodb+srv://..."

    # The URL of your LIVE Hugging Face Space
    HF_BACKEND_API_URL="[https://your-hf-space-name.hf.space/api/chat](https://your-hf-space-name.hf.space/api/chat)"
    ```

3.  **Install dependencies:**
    ```sh
    npm install
    ```

4.  **Run the server:**
    ```sh
    npm start
    ```
    The logic backend will now be running at **`http://localhost:8000`**. Keep this terminal open.

---

### Step 2: Run the Frontend (React)

In a **new terminal window**, set up and run the React frontend.

1.  **Navigate to the `frontend` directory:**
    ```sh
    cd frontend
    ```

2.  **Create an `.env.local` file:**
    Create a file named `.env.local` in the `frontend` directory. It must point to your *local logic backend*.
    ```.env.local
    REACT_APP_API_URL="http://localhost:8000/api/chat"
    ```

3.  **Install dependencies:**
    ```sh
    npm install
    ```

4.  **Run the app:**
    ```sh
    npm start
    ```

Your browser will open to **`http://localhost:3000`**. The application is now fully running!

---

## Deployment

This 3-tier application has a separate deployment strategy for each part:

* **`frontend`:** A static React site, perfect for deployment on platforms like **Netlify**, **Vercel**, or GitHub Pages.
* **`Backend`:** A lightweight Node.js server. It can be deployed on any service that supports Node.js, such as **Render**, **Heroku**, or a small cloud VM.
* **`HF_Backend`:** A heavy Python/FastAPI application. It is containerized with Docker and requires a **GPU-enabled** host for good performance, such as **Hugging Face Spaces** (using a T4 GPU) or a dedicated cloud GPU instance.

---

## Notes & Recommendations

* If you *do* want to run the `HF_Backend` locally, you will need a powerful **NVIDIA GPU** with CUDA support. You would start it in a separate terminal and change the `HF_BACKEND_API_URL` in your `.env` file to `http://localhost:7860/api/chat`.
* Monitor logs for model download/progress during first startup — model files can be large.
* Keep sensitive keys and secrets out of the repository — use environment variables for configuration.

---

## License

Distributed under the **MIT License**. See `LICENSE` for more information.

## Thank you

Thank you for checking out **Cern** — contributions, feedback, and bug reports are very welcome.