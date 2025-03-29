import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
