import os

class Config:
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    GEMINI_MODEL = "gemini-2.0-flash"  # Lighter than 3-flash-preview
    
    GOOGLE_SEARCH_API_KEY = os.environ.get('GOOGLE_SEARCH_API_KEY', '')
    GOOGLE_SEARCH_ENGINE_ID = os.environ.get('GOOGLE_SEARCH_ENGINE_ID', '')
    
    ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY', '')
    ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
    
    DATABASE_PATH = "saiman_memory.db"
    USER_NAME = "Saiman"