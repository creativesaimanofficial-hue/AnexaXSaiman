"""
DeepSeek API - Free AI Engine for Anexa
"""

import requests
import logging

logger = logging.getLogger("DeepSeekEngine")

class DeepSeekEngine:
    def __init__(self, api_key):
        self.api_key = api_key
        self.available = False
        self.api_url = "https://api.deepseek.com/v1/chat/completions"
        
        if api_key:
            self.available = True
            logger.info("✅ DeepSeek API ready! (5M free tokens!)")
    
    def generate_response(self, user_input, context):
        if not self.available:
            return None
        
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            
            data = {
                "model": "deepseek-chat",
                "messages": [
                    {"role": "system", "content": context},
                    {"role": "user", "content": user_input}
                ],
                "temperature": 0.85,
                "max_tokens": 500
            }
            
            response = requests.post(self.api_url, headers=headers, json=data, timeout=30)
            
            if response.status_code == 200:
                result = response.json()
                return result["choices"][0]["message"]["content"]
            else:
                logger.error(f"DeepSeek error: {response.status_code}")
                return None
                
        except Exception as e:
            logger.error(f"DeepSeek error: {e}")
            return None