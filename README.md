# FAST Content AI

A modular, production-ready backend for AI-powered article generation and content management. Built using the Flask backend, it integrates OpenAI/Groq LLMs, MongoDB, and Celery for background tasks, and includes full unit testing. Designed for scalability, testability, and rapid development.

---

## 🚀 Features

- **Website Registration:**  
  Websites register their domain (and optionally a custom `website_id`). They can later fetch articles using API requests.

- **Article Generation:**  
  Articles are generated automatically using an LLM (OpenAI's GPT‑3.5‑turbo or a local LLaMA model). Each article includes:
  - Title
  - Content
  - Image URL
  - Published date
  - Metadata (tags, author, extra info for future use)

- **API Endpoints:**
  - `POST /api/webhook/register`: Register a website.
  - `GET /api/articles?website_id=<id>`: Retrieve all articles for a website.
  - `GET /api/article/<article_id>`: Retrieve a specific article by ID.
  - `GET /api/test_generate/<website_id>`: Test endpoint to generate and store an article.

---

## ⚙️ Setup

```bash
# Install dependencies
pip install -r requirements.txt

# .env file (create this in the root directory)
# ----------------------------------------------
MONGODB_URI="mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+2.5.0"
DATABASE_NAME="content_db"
FLASK_HOST="0.0.0.0"
FLASK_PORT=3000
LLM_TYPE="llama"
OPENAI_API_KEY="your_openai_api_key_here"
GROK_API_KEY="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"
PAPA="llama"
# ----------------------------------------------

# Run the Flask app
python app.py

# Run Celery worker
celery -A tasks.celery_app worker --loglevel=info

# Run unit tests
python -m unittest discover tests

# Create empty log file
mkdir -p logs
touch logs/app.log
