"""
Google Gemini API - Free AI Engine for Anexa
Gemini 3 Flash Preview - Latest Free Model
"""

import google.generativeai as genai
import logging

logger = logging.getLogger("GeminiEngine")

class GeminiEngine:
    def __init__(self, api_key, model_name="gemini-3-flash-preview"):
        self.api_key = api_key
        self.model_name = model_name
        self.available = False
        
        if api_key:
            try:
                genai.configure(api_key=api_key)
                
                # Try the specified model first
                try:
                    self.model = genai.GenerativeModel(model_name)
                    self.available = True
                    logger.info(f"✅ Gemini initialized with: {model_name}")
                except Exception as e:
                    # Fallback to gemini-2.0-flash
                    logger.warning(f"Model {model_name} not available, trying gemini-2.0-flash")
                    try:
                        self.model = genai.GenerativeModel('gemini-2.0-flash')
                        self.available = True
                        logger.info("✅ Gemini initialized with: gemini-2.0-flash")
                    except:
                        # Final fallback
                        try:
                            self.model = genai.GenerativeModel('gemini-flash-latest')
                            self.available = True
                            logger.info("✅ Gemini initialized with: gemini-flash-latest")
                        except:
                            logger.error("❌ No Gemini models available")
                        
            except Exception as e:
                logger.error(f"Gemini init failed: {e}")
    
    def generate_response(self, user_input, context):
        """Generate response using Gemini"""
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