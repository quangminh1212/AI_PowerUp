<!-- source: https://github.com/anxmeshhh/ChampBot-AI.git sha: b48b8f8c7abbc6fc03bc6eda3f516783389d15f2 readme: main/README.md -->
# anxmeshhh/ChampBot-AI

A Flask-based conversational career coach that stores user profiles, conversation memory, goals, and AI-generated insights. Built with Flask + SQLAlchemy; includes memory & goal management and Groq-powered insight generation.

---

# ChampBot — Career Cosmos AI Coach 🤖🎯

A Flask-based conversational career coach that stores user profiles, conversation memory, goals, and AI-generated insights. Built with Flask + SQLAlchemy; includes memory & goal management and Groq-powered insight generation.

---

## ✅ Key Features
- User registration & login (SQLAlchemy models) 🔐
- Chat endpoint with AI responses, persona detection, and feature-based responses 💬
- Automatic conversation memory extraction and persistence (topics, pain points, etc.) 🧠
- Goal CRUD (create, update, delete) and progress tracking 📋
- AI-generated actionable insights using Groq model (JSON output) 🔮
- Profile, history, memory stats, snapshots, and insights endpoints for client apps 📈
- CORS enabled for easy frontend integration 🌐

---

## Quickstart — Prerequisites & Setup 🔧

1. Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
# source venv/bin/activate  # macOS / Linux
```

2. Install dependencies:

```bash
pip install -r requirements.txt
# If not present, install at least: flask flask-cors sqlalchemy python-dotenv groq
```

3. Environment variables (create a `.env` file in `champbot/` or project root):

```env
SECRET_KEY=your_secret_key_here
DATABASE_URI=sqlite:///path/to/your.db   # optional; defaults to champbot/database/career_cosmos.db
GROQ_API_KEY=your_groq_api_key_here      # required for insight generation
# Optional provider keys: GEMINI_API_KEY, ANTHROPIC_API_KEY, OPENAI_API_KEY
```

4. Run the app:

```bash
cd career_counseling/champbot
python app.py
```

App runs in debug mode by default on `http://localhost:5010`.

Notes:
- The app uses `db.create_all()` at startup to create tables automatically (no migrations configured).
- Config is read from `champbot/config.py` (environment overrides allowed).

---

## Important Config & Env Vars ⚙️
- `SECRET_KEY` — set securely in env for production (do not use default) 🔒
- `DATABASE_URI` — SQLAlchemy DB URI (defaults to `champbot/database/career_cosmos.db`) 🗃️
- `GROQ_API_KEY` — required for `generate_insight` (Groq chat completions) 🤖
- Optional AI keys: `GEMINI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`

---

## HTTP Endpoints (selected) 🧭
- GET `/` — Serve main UI (`templates/index.html`)
- POST `/api/auth/register` — Register: JSON body `{ username, email, password }`
- POST `/api/auth/login` — Login: JSON body `{ username, password }` → returns user and stats
- POST `/api/chat` — Chat with AI: `{ user_id, message, persona?, feature? }` → returns `response`, `persona`, `stats`
- GET `/api/history/<user_id>` — Get recent conversation history
- GET/POST `/api/profile/<user_id>` — Get or update user profile
- Goals endpoints: `/api/goals/<user_id>` and `/api/goals/<user_id>/<goal_id>` (GET/POST/PUT/DELETE)
- GET `/api/memory/<user_id>` — Retrieve conversation memory
- GET `/api/insights/<user_id>` — Fetch AI-generated insights
- POST `/api/generate-insight/<user_id>` — Generate a new insight using recent conversations (uses Groq)
- GET `/api/memory-stats/<user_id>` — Return aggregated memory & conversation stats

---

## Internals & Notes 🔍
- Models: `champbot/database/models.py` (User, Conversation, Goal, Memory, Insight, etc.)
- AI logic: `champbot/utils/ai_handler.py` — persona detection and feature handlers
- `auto_save_conversation_memory` extracts topics and pain points from messages and writes to DB
- Insight generation uses Groq chat completion and expects JSON output to parse into `UserInsight`

---

## Troubleshooting & Common Fixes ⚠️
- DB folder is created automatically (`champbot/database/`) — ensure write permissions.
- If insights fail, verify `GROQ_API_KEY` is set and valid.
- For missing imports, ensure `pip install -r requirements.txt` completed successfully.
- For production, set `debug=False` and run behind a WSGI server (Gunicorn/uWSGI).

---

## Security & Production Recommendations 🔒
- Replace default `SECRET_KEY` with a secure, random value.
- Run app under HTTPS behind a reverse proxy.
- Use proper DB migrations (Flask-Migrate) instead of `create_all()` for schema changes.
- Rotate API keys and keep them out of VCS.

---

## Contributing & Next Steps ✨
- Add tests for key endpoints and persistence behaviors.
- Add migrations (Alembic/Flask-Migrate) and CI test workflow.
- Consider rate-limiting and authentication tokens (JWT) for production readiness.

---

If you want, I can open a PR with this README or commit it directly — tell me which you prefer.