<!-- source: https://github.com/Ameershaik3288/Ameer-Chat-Bot.git sha: 4b3edca3603157b857fd817c52ae30957b295bd1 readme: main/README.md -->
# Ameershaik3288/Ameer-Chat-Bot

Chat Bot is a lightweight web-based AI chat assistant built with Flask and powered by Google Gemini 2.5 Flash, featuring a modern UI for real-time conversational AI interactions.

---

🤖 Ameer AI – Flask + Gemini Chat Assistant

A sleek, futuristic AI chat assistant built using Flask and Google Gemini 2.5 Flash, featuring a modern UI and real-time AI responses.
Designed for experimentation, learning, and building next-gen AI assistants.

🚀 Features

🔥 Gemini 2.5 Flash powered responses

🧠 Flask backend with REST API

🎨 Modern Tailwind-based chat UI

⚡ Real-time chat interaction

🖥️ Localhost deployment ready

🧩 Clean & beginner-friendly structure

📁 Project Structure

├── main.py

├── templates/

│   └── index.html

└── README.md

🛠️ Tech Stack

Frontend: HTML, Tailwind CSS, JavaScript

Backend: Python, Flask

AI Model: Google Gemini 2.5 Flash

API Client: google-generativeai (genai)

🔑 Prerequisites

Make sure you have:

Python 3.9+

A Google Gemini API Key

pip (Python package manager)

⚙️ Configuration

Open main.py and replace:

client = genai.Client(api_key="Your API KEY")

with your actual Gemini API key.

🔒 Tip: Never commit your real API key to GitHub.
Use environment variables for production.

▶️ Run the Application

python main.py

The app will start at:

http://127.0.0.1:5000

🧠 How It Works

1.User sends a message from the UI

2.JavaScript sends it to /chat endpoint

3.Flask forwards it to Gemini 2.5 Flash

4.Gemini generates a response

5.Response is displayed in real-time

🌱 Future Enhancements

🎤 Voice input (Jarvis mode)

🧠 Multi-agent AI roles

😄 Emotion-aware responses

🌐 Deployment on cloud

🔐 API key via .env

👨‍💻 Author

Shaik Ameer Hussain
AI | Data Science | GenAI | Startup Builder

🔗 GitHub: https://github.com/Ameershaik3288

⭐ Support

If you like this project, give it a star ⭐
and feel free to fork, improve, or build on top of it!
