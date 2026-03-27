import os

class Config:
    # ============ DEEPSEEK API ============
    DEEPSEEK_API_KEY = os.environ.get('DEEPSEEK_API_KEY', '')
    USE_DEEPSEEK = False  # ← SET TO FALSE TO USE FALLBACK
    
    # ============ GOOGLE SEARCH ============
    GOOGLE_SEARCH_API_KEY = os.environ.get('GOOGLE_SEARCH_API_KEY', '')
    GOOGLE_SEARCH_ENGINE_ID = os.environ.get('GOOGLE_SEARCH_ENGINE_ID', '')
    
    # ============ ELEVENLABS VOICE ============
    ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY', '')
    ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
    
    DATABASE_PATH = "saiman_memory.db"
    USER_NAME = "Saiman"