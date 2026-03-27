"""
Google Gemini 3 Flash API - Free AI Engine for Anexa
"""

import google.generativeai as genai
import logging

logger = logging.getLogger("GeminiEngine")

class GeminiEngine:
    def __init__(self, api_key):
        self.api_key = api_key
        self.available = False
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                # Using Gemini 3 Flash - Latest free model
                self.model = genai.GenerativeModel('gemini-3-flash')
                self.available = True
                logger.info("✅ Gemini 3 Flash API initialized (FREE)")
            except Exception as e:
                logger.error(f"Gemini init failed: {e}")
    
    def generate_response(self, user_input, context):
        """Generate response using Gemini 3 Flash"""
        if not self.available:
            return None
        
        try:
            full_prompt = f"""{context}

User: {user_input}

Anexa:"""
            
            response = self.model.generate_content(full_prompt)
            return response.text
        except Exception as e:
            logger.error(f"Gemini error: {e}")
            return None