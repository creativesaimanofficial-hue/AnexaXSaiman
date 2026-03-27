"""
Google Gemini API - Lightweight Version for Free Tier
"""

import google.generativeai as genai
import logging

logger = logging.getLogger("GeminiEngine")

class GeminiEngine:
    def __init__(self, api_key, model_name="gemini-2.0-flash"):
        self.api_key = api_key
        self.available = False
        
        if api_key and api_key.strip():
            try:
                # Minimal configuration
                genai.configure(api_key=api_key)
                self.model = genai.GenerativeModel(model_name)
                self.available = True
                logger.info(f"✅ Gemini ready with: {model_name}")
            except Exception as e:
                logger.error(f"Gemini init failed: {e}")
    
    def generate_response(self, user_input, context):
        if not self.available:
            return None
        
        try:
            # Use shorter prompt to save memory
            full_prompt = f"{context}\n\nUser: {user_input}\n\nAnexa:"
            
            response = self.model.generate_content(
                full_prompt,
                generation_config={
                    "temperature": 0.85,
                    "max_output_tokens": 300,  # Reduced from 500
                }
            )
            return response.text
        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return None