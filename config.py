"""
ANEXA GF4 - Configuration
All API Keys from Environment Variables
"""

import os

class Config:
    """Master configuration for Anexa AI Girlfriend"""
    
    # ============ OPENAI (ChatGPT) - FROM ENVIRONMENT ============
    OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', '')
    OPENAI_MODEL = "gpt-4o-mini"  # Free model - works without payment
    OPENAI_MAX_TOKENS = 500
    OPENAI_TEMPERATURE = 0.85
    
    # ============ GOOGLE SEARCH - FROM ENVIRONMENT ============
    GOOGLE_SEARCH_API_KEY = os.environ.get('GOOGLE_SEARCH_API_KEY', '')
    GOOGLE_SEARCH_ENGINE_ID = os.environ.get('GOOGLE_SEARCH_ENGINE_ID', '')
    
    # ============ ELEVENLABS VOICE - FROM ENVIRONMENT ============
    ELEVENLABS_API_KEY = os.environ.get('ELEVENLABS_API_KEY', '')
    ELEVENLABS_VOICE_ID = "21m00Tcm4TlvDq8ikWAM"  # Rachel voice
    
    # ============ DATABASE ============
    DATABASE_PATH = "saiman_memory.db"
    
    # ============ USER ============
    USER_NAME = "Saiman"