import os
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-only-change-me")
    DATABASE = os.path.join(BASE_DIR, "instance", "artopia.db")
    UPLOAD_FOLDER = os.path.join(BASE_DIR, "app", "static", "uploads")
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # reject uploads over 5 MB
    AI_API_KEY = os.environ.get("AI_API_KEY")