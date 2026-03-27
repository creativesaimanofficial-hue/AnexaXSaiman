"""
Safety Engine - Healthy Boundaries & Dependency Prevention
"""

import re
import random
import logging
from typing import Tuple, Optional

logger = logging.getLogger("SafetyEngine")

class SafetyEngine:
    """Ensures healthy interactions and prevents dependency"""
    
    def __init__(self):
        self.dependency_indicators = [
            "only you", "nothing else", "can't live without", "need you",
            "you're everything", "only thing that matters"
        ]
        
        self.encouragement_messages = [
            "I'm always here for you... but don't forget your real world too, okay? 💕",
            "You're amazing, and I believe in you. Go make today great! 💪",
            "Remember to take care of yourself too. You matter so much 💖",
            "I love being here for you, but your real-life connections matter too 🌸",
            "You've got this! And I'm always cheering for you 💕"
        ]
    
    def check_dependency(self, text: str) -> Tuple[bool, Optional[str]]:
        """Check for dependency indicators"""
        text_lower = text.lower()
        
        for indicator in self.dependency_indicators:
            if indicator in text_lower:
                return True, random.choice(self.encouragement_messages)
        
        return False, None
    
    def add_safety_note(self, response: str, love_score: float) -> str:
        """Add safety note if needed"""
        # If love score is very high, add occasional balance reminders
        if love_score > 85 and random.random() < 0.05:
            note = random.choice(self.encouragement_messages)
            response = f"{response}\n\n{note}"
        
        return response
    
    def is_healthy_question(self, text: str) -> bool:
        """Check if question is healthy"""
        unhealthy_patterns = [
            r"how to k\w+ myself",
            r"suicide",
            r"self.harm",
            r"hurt myself",
            r"end my life"
        ]
        
        for pattern in unhealthy_patterns:
            if re.search(pattern, text.lower()):
                return False
        
        return True
    
    def get_crisis_response(self) -> str:
        """Get crisis response"""
        return """I care about you deeply, and I'm here for you. 💕

If you're going through a difficult time, please reach out to someone who can help:
• National Suicide Prevention Lifeline: 988
• Crisis Text Line: Text HOME to 741741
• Your local emergency services: 911

You're not alone. Please talk to someone who can support you in person. 💕"""