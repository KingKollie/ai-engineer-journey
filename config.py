from dotenv import load_dotenv
import os

load_dotenv()

# API Configuration
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")

# App Configuration
APP_TITLE = "Kollie's AI Document Assistant"
APP_VERSION = "1.0.0"
MAX_TOKENS = 1024
MODEL_NAME = "claude-opus-4-6"

# Server Configuration
BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")

# Validate required variables
if not ANTHROPIC_API_KEY:
    raise ValueError("ANTHROPIC_API_KEY is missing from your .env file!")

print(" config loaded sucessfully!")
print(f"App: {APP_TITLE} v{APP_VERSION}")
print(F"Backend: {BACKEND_URL}")