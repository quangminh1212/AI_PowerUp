<!-- source: https://github.com/Kritika-Kanchan-dev/NexaVoice-IDE.git sha: dda991c523537d77294b30045c5f9df72ac3dcd9 readme: main/README.md -->
# Kritika-Kanchan-dev/NexaVoice-IDE

NexaVoice IDE is an advanced AI-powered coding assistant built for The Claude Challenge Hackathon. It combines voice-to-code, AI debugging, auto-fixing, code generation, and MongoDB-powered history in one clean, powerful interface.

---

# 🚀 NexaVoice IDE  – AI-Powered Voice Coding IDE  
### Built by Team **NexaByte**

NexaVoice IDE  is an advanced AI-powered coding assistant built for The Claude Challenge Hackathon.  
It combines **voice-to-code**, **AI debugging**, **auto-fixing**, **code generation**, and **MongoDB-powered history** in one clean, powerful interface.

This project showcases real-world developer productivity tools enhanced by **Gemini 1.5 Flash**, **Flask backend**, **MongoDB Atlas**, and a **modern Tailwind UI**.

---

# ✨ Features

## 🧠 AI Features
- **AI Debugging** – Find errors, line numbers, and suggested fixes  
- **Auto Code Fixing** – Instantly fix broken code  
- **Code Generation** – Generate complete code from natural language  
- **Test Case Generator** – Creates Python unittest boilerplates  
- **Code Formatting** – Clean output without markdown noise  

## 🎙 Voice Features
- **Voice-to-Code Input** using Web Speech API  
- Speak instructions and instantly convert them into code  
- Perfect for hands-free coding  

## 💾 MongoDB History (Atlas Cloud)
- Debug history  
- Auto-fix history  
- Code generation history  
- Timestamped & organized collections  

## 💻 UI & UX
- Responsive Tailwind-based interface  
- Fast, lightweight, fully browser-based frontend  
- Copy buttons, clean formatting, and smooth workflow  

## 🌐 Deployment
- **Frontend** → Vercel  
- **Backend** → Render  
- **Database** → MongoDB Atlas  
- 100% cloud-based and fully scalable  

---

# 🏗️ Project Architecture

Frontend (Vercel Hosting)
|
|-- fetch API calls --> Backend API (Render)
|
|-- Gemini-pro-latest (Google API)
|
|-- MongoDB Atlas (Cloud Database)


---

# 📁 Folder Structure

Claude_Challenge/
│
├── backend/
│ ├── app.py
│ ├── llm_handler.py
│ ├── db.py
│ ├── .env
│ └── requirements.txt
│
├── frontend/
│ ├── app.js
│ ├── debug.html
│ └── index.html
│
├── README.md
└──requirements.txt

---

# ⚙️ Tech Stack

### **Frontend**
- HTML, JavaScript  
- Tailwind CSS (CDN version)  
- Web Speech API  

### **Backend**
- Python (Flask)  
- Flask-CORS  
- Gunicorn (production)  
- Google Generative AI (gemini-pro-latest)  

### **Database**
- MongoDB Atlas (Cloud)  
- PyMongo  

---

# 📦 Installation (Local Development)

## 1️⃣ Clone the Backend
```bash
git clone https://github.com/Kritika-Kanchan-dev/nexabyte-backend.git
cd nexabyte-backend
```

## 2️⃣ Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate
```

## 3️⃣ Install Requirements
```bash
pip install -r requirements.txt
```

## 4️⃣ Add Environment Variables
```bash
GEMINI_API_KEY=your_gemini_key
MONGO_URI=your_mongo_atlas_url
DB_NAME=codeide
```

## 5️⃣ Run Backend Locally
```bash
python app.py
```
- Backend will run at: http://127.0.0.1:5000

# 🎨 Run Frontend Locally

## Open a terminal inside /frontend:
```bash
cd frontend
python -m http.server 8000
```

## Open:
```bash
http://localhost:8000/index.html
```

# 🌐 Deployment Guide

## 🚀 Backend Deployment (Render)

- Push backend folder to GitHub

- Create Render Web Service

- Set Build Command:

```bash
pip install -r requirements.txt
```

- Start Command:

```bash
gunicorn app:app
```

- Add environment variables

- Deploy → Get backend URL

## 🚀 Frontend Deployment (Vercel)

- Push frontend folder to GitHub

- Import repo into Vercel

- Select Static Website

- Deploy

- Update this line in app.js:

- const API_URL = "https://your-backend-url.onrender.com";

## Your live site is ready 🎉

# 🧪 Example Prompts to Try
### Debug:
```bash
def add(a, b):
    return a + c
print(add(2, 3))
```

### Generate Code:

- create a python student management system with add update delete list features

### Voice Command:

- “Write a Python class for a calculator.”

---

### All Important Links
- Backend Repo: [https://github.com/.../nexavoice-ide-backend](https://github.com/Kritika-Kanchan-dev/nexavoice-ide-backend)
- Frontend Repo: [https://github.com/.../nexavoice-ide-frontend](https://github.com/Kritika-Kanchan-dev/nexavoice-ide-frontend)
- Master Repo: [https://github.com/.../NexaVoice-IDE](https://github.com/Kritika-Kanchan-dev/NexaVoice-IDE)
- Live Frontend: [https://nexavoice-ide-frontend.vercel.app](https://nexavoice-ide-frontend.vercel.app/)
- Live Backend: [https://nexavoice-ide-backend-1.onrender.com](https://nexavoice-ide-backend-1.onrender.com)

# ❤️ Why NexaVoice IDE?

Because developers deserve a coding assistant that understands:
- ✔ Voice
- ✔ Code
- ✔ Errors
- ✔ Fixes
- ✔ History

NexaVoice IDE is built to make coding faster, smarter, and more human-friendly.
