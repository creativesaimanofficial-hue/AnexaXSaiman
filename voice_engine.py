"""
Voice Engine - ElevenLabs Integration
"""

import requests
import base64
import logging
from config import Config

logger = logging.getLogger("VoiceEngine")

class VoiceEngine:
    """ElevenLabs voice synthesis"""
    
    def __init__(self):
        self.api_key = Config.ELEVENLABS_API_KEY
        self.voice_id = Config.ELEVENLABS_VOICE_ID
        self.enabled = bool(self.api_key)
    
    def synthesize(self, text: str, emotion: str = "neutral") -> Optional[bytes]:
        """Convert text to speech"""
        if not self.enabled:
            return None
        
        try:
            url = f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}"
            headers = {
                "Accept": "audio/mpeg",
                "Content-Type": "application/json",
                "xi-api-key": self.api_key
            }
            
            # Adjust voice settings based on emotion
            stability = 0.5
            similarity_boost = 0.75
            
            if emotion == "happy":
                stability = 0.4
                similarity_boost = 0.8
            elif emotion == "sad":
                stability = 0.7
                similarity_boost = 0.6
            elif emotion == "romantic":
                stability = 0.5
                similarity_boost = 0.8
            elif emotion == "playful":
                stability = 0.3
                similarity_boost = 0.85
            
            data = {
                "text": text,
                "model_id": "eleven_monolingual_v1",
                "voice_settings": {
                    "stability": stability,
                    "similarity_boost": similarity_boost
                }
            }
            
            response = requests.post(url, json=data, headers=headers, timeout=10)
            
            if response.status_code == 200:
                return response.content
            else:
                logger.error(f"ElevenLabs error: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"Voice synthesis error: {e}")
            return None