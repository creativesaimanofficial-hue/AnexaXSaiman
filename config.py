"""
ANEXA Configuration - Using Google Gemini 3 Flash
"""

import os

class Config:
    """Master configuration for Anexa AI Girlfriend"""
    
    # ============ GEMINI API (FREE - Latest Model) ============
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY', '')
    GEMINI_MODEL = "gemini-3-flash"  # Latest free model
    
    # ============ GOOGLE SEARCH ============
    GOOGLE_SEARCH_API_KEY = os.environ.get('GOOGLE_SEARCH_API_KEY', '')
    GOOGLE_SEARCH_ENGINE_ID = os.environ.get('GOOGLE_SEARCH_ENGINE_ID', '')
    
    # ============ ELEVENLABS VOICE ============
    ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY', '')
    ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"
    
    # ============ DATABASE ============
    DATABASE_PATH = "saiman_memory.db"
    
    # ============ USER ============
    USER_NAME = "Saiman"