"""
Google Custom Search Engine
Real-time web search integration
"""

import requests
from typing import Optional
import logging
from config import Config

logger = logging.getLogger("SearchEngine")

class SearchEngine:
    """Google Custom Search integration"""
    
    def __init__(self):
        self.api_key = Config.GOOGLE_SEARCH_API_KEY
        self.engine_id = Config.GOOGLE_SEARCH_ENGINE_ID
        self.enabled = bool(self.api_key and self.engine_id)
    
    def search(self, query: str, num_results: int = 2) -> Optional[str]:
        """Search the web and return results"""
        if not self.enabled:
            return None
        
        try:
            url = "https://www.googleapis.com/customsearch/v1"
            params = {
                "key": self.api_key,
                "cx": self.engine_id,
                "q": query,
                "num": num_results
            }
            
            response = requests.get(url, params=params, timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                results = []
                
                for item in data.get("items", []):
                    title = item.get("title", "")
                    snippet = item.get("snippet", "")
                    if snippet:
                        results.append(snippet)
                
                if results:
                    return " ".join(results)
            
            return None
            
        except Exception as e:
            logger.error(f"Search error: {e}")
            return None