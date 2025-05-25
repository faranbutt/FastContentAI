# config.py

import os
from dotenv import load_dotenv
load_dotenv()
load_dotenv(dotenv_path=".env")

# MongoDB settings
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "content_db")

# Flask settings
FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))

# LLM settings
LLM_TYPE = os.getenv("PAPA")  # This will now be fetched from .env
print(LLM_TYPE)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
GROQ_API_KEY = os.getenv("GROK_API_KEY", "")
print(GROQ_API_KEY)
LLAMA_MODEL_NAME = os.getenv("LLAMA_MODEL_NAME", "meta-llama/Llama-2-7b-chat-hf")


# # MongoDB settings
# MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")
# DATABASE_NAME = os.getenv("DATABASE_NAME", "content_db")

# # Flask settings
# FLASK_HOST = os.getenv("FLASK_HOST", "0.0.0.0")
# FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))

# # Celery settings (if asynchronous tasks are used)
CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL", "redis://localhost:6379/0")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND", "redis://localhost:6379/0")

# # LLM settings
# LLM_TYPE = os.getenv("LLM_TYPE", "llama")  # Options: "openai" or "llama"

# # Llama API keys
# GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")  # For Groq Llama integration
# # HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY", "")  # Uncomment for Hugging Face Llama

# # For Hugging Face (if using a local model or hosted model)
# LLAMA_MODEL_NAME = os.getenv("LLAMA_MODEL_NAME", "meta-llama/Llama-2-7b-chat-hf")


# # For OpenAI (GPT-3.5-turbo)
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
