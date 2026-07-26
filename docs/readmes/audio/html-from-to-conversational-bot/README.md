<!-- source: https://github.com/Aditya-Agrahari1/Html-From-To-Conversational-bot.git sha: 76447d975ed86da74525c7a51c91647261f5bc69 readme: main/README.md -->
# Aditya-Agrahari1/Html-From-To-Conversational-bot

Convert static HTML forms into intelligent, voice-ready, AI-powered conversational flows. FormX is a full-stack open-source tool that transforms any HTML form into a smart chatbot interface -with support for multi-step interaction, real-time validation, TTS/STT. Ideal for modern lead generation, event registrations, or personalized data collection.

---

# FormX🧩
 
A full-stack web application that integrates a powerful frontend interface with a Python-based backend to deliver seamless form submission and processing capabilities.

---

## 🚀 Project Structure

This project is organized into two main branches:

- `frontend` – Vite + React-based user interface.
- `backend` – FastAPI-based Python backend for handling form submissions.

The `main` branch contains only the project overview and documentation.

---

## 🧪 Getting Started

Follow these steps to run the project locally:

---

## 📦 1. Clone the Repository

> ⚠️ To work on both the frontend and backend simultaneously, **clone the repo twice** into separate folders and switch each to the appropriate branch.

```bash
# Clone the frontend branch
git clone -b frontend https://github.com/Aditya-Agrahari1/conversa-form-magic.git conversa-frontend

# Clone the backend branch
git clone -b backend https://github.com/Aditya-Agrahari1/conversa-form-magic.git conversa-backend
```

---

## 🌐 2. Run the Frontend

> 📁 Navigate to the `conversa-frontend` folder

### 🔧 Requirements: [Node.js](https://nodejs.org)

```bash
cd conversa-frontend

# Install dependencies
npm install

# Start the development server
npm run dev
```

🔗 This will launch the frontend at: `http://localhost:5173`

---

## 🧠 3. Run the Backend

> 📁 Open a **new terminal** and navigate to the `conversa-backend` folder

### 🐍 Requirements: Python 3.13+

```bash
cd conversa-backend

# Install Python dependencies
pip install -r requirements.txt

# Start the FastAPI server
uvicorn main:app --reload
```

🔗 This will launch the backend at: `http://127.0.0.1:8000`

---

## 🛠 Tech Stack

- **Frontend:** React + Vite + TailwindCSS + ShadCN
- **Backend:** FastAPI (Python)
- **Dev Tools:** VS Code, Git, GitHub

---

## 📂 Branch Overview

| Branch     | Description                |
|------------|----------------------------|
| `main`     | Project overview (docs only) |
| `frontend` | Frontend Vite + React code |
| `backend`  | Python FastAPI backend     |

---



## 📌 Progress Updates

- ✅ **Frontend + Backend integration is complete**  
  - Users can upload an HTML form or paste a form URL  
  - Chatbot parses the form and guides the user through each field  
  - Multi-language support (e.g., Hindi, Tamil, English) is fully working  

- ✅ **Auto-filling and submitting the original form**  
  - Form is filled using **Selenium** or **Playwright**  
  - System takes a screenshot after submission and returns it to the user  

- ✅ **Input validation and field correction handling**  
  - Detects off-topic or invalid inputs (e.g., "hello" instead of a phone number)  
  - Users can correct earlier responses mid-conversation (e.g., “Actually, my name is Shivam”)
  - **New:** Date of Birth inputs are auto-formatted using `datetime` (e.g., "1 Aug 2004" → "01-08-2004")  


- ✅ **File/media upload support**  
  - Handles image or document uploads with skip option  
  - "📤 uploaded" messages are parsed intelligently  

- ✅ **Real-time visual field summary + emoji progress bar**  
  - Live side panel shows what fields are filled so far  
  - Emoji progress updates after each step (e.g., `🟩🟩🟦🟦 (2 of 4 completed)`)  

- ✅ **Text-to-Speech (TTS) support using edge-tts**  
  - Bot responses are spoken aloud  
  - Voice is matched to user’s selected language (e.g., Hindi, Tamil)  
  - Text is shown only after TTS is ready, ensuring smooth sync  

- ✅ **Security Warning for Sensitive Fields (e.g., password)**  
  - If the uploaded form contains a password field, the bot warns the user  
  - Options:  
    1. "I agree to enter my password" (continue)  
    2. "Open original form" (redirect to original website)  

- ✅ **Robust URL Validation & Feedback**  
  - ⚠ Invalid URL: prompts user to enter a valid URL format  
  - ⚠ Unreachable URL: shows user-friendly connection error  
  - ⚠ No form/input elements: alerts user that the page has no form to fill  
  - ⚠ Input without `<form>`: warns user the structure is not submittable  
  - ⚠ JS-generated/dynamic forms: suggests uploading static `.html` file  

- ✅ **UI Enhancements**  
  - Clean dark mode, soft gradients, animated transitions  
  - Submit CTA appears only after all fields are answered  
  - Feedback form included  

- ✅ API Version (New!)  
  - All backend logic is now exposed via clean `/api/*` endpoints  
  - Consistent JSON structure (`success`, `data`, `error`)  
  - Full Swagger docs available at [http://localhost:8000/docs](http://localhost:8000/docs)
 
    
- 🔧 **Current focus**  
  - Minor bug fixes  
  - Judge-only debug mode: audit logs + JSON dump  
  - Final README polish and demo recording

  
---

## 🤝 Contributing

Pull requests are welcome! Feel free to fork the repo and submit a PR on the respective branch (`frontend` or `backend`).

## 📄 License

This project is under the Apache-2.0 License. See `LICENSE` for details.

---
