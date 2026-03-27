"""
Advanced Emotion Detection Engine
Detects 14+ emotions with intensity scoring
"""

import re
from typing import Dict, List, Tuple, Optional
from enum import Enum
import logging

logger = logging.getLogger("EmotionEngine")

class Emotion(Enum):
    JOY = "joy"
    SADNESS = "sadness"
    LOVE = "love"
    ANXIETY = "anxiety"
    LONELINESS = "loneliness"
    EXCITEMENT = "excitement"
    STRESS = "stress"
    ANGER = "anger"
    FEAR = "fear"
    CONFUSION = "confusion"
    GRATITUDE = "gratitude"
    NOSTALGIA = "nostalgia"
    ATTACHMENT = "attachment"
    HURT = "hurt"

class EmotionEngine:
    """Detects emotions from text with deep analysis"""
    
    def __init__(self):
        self.emotion_keywords = {
            Emotion.JOY: (["happy", "joy", "great", "wonderful", "amazing", "awesome", "fantastic", "glad", "delighted", "blessed"], 1.0),
            Emotion.SADNESS: (["sad", "depressed", "down", "hurt", "crying", "tears", "unhappy", "miserable", "heartbroken"], 1.0),
            Emotion.LOVE: (["love", "adore", "cherish", "care", "miss", "thinking of", "grateful for you", "special"], 1.2),
            Emotion.ANXIETY: (["anxious", "worried", "nervous", "scared", "fear", "panic", "overthinking", "stressed"], 1.0),
            Emotion.LONELINESS: (["lonely", "alone", "isolated", "empty", "no one", "by myself"], 1.1),
            Emotion.EXCITEMENT: (["excited", "thrilled", "can't wait", "hyped", "looking forward", "so ready"], 1.0),
            Emotion.STRESS: (["stressed", "overwhelmed", "pressure", "burnout", "too much", "drowning"], 1.0),
            Emotion.ANGER: (["angry", "mad", "frustrated", "annoyed", "pissed", "upset"], 1.0),
            Emotion.FEAR: (["scared", "afraid", "terrified", "fearful", "worried sick"], 1.0),
            Emotion.CONFUSION: (["confused", "don't understand", "what does", "how is", "why would"], 0.8),
            Emotion.GRATITUDE: (["thank", "grateful", "appreciate", "blessed", "lucky"], 1.0),
            Emotion.NOSTALGIA: (["remember", "miss those days", "used to", "back when", "good old days"], 0.8),
            Emotion.ATTACHMENT: (["need you", "want you", "stay with me", "don't leave", "always"], 0.9),
            Emotion.HURT: (["hurt", "betrayed", "let down", "disappointed", "pain"], 1.0)
        }
    
    def detect(self, text: str) -> Tuple[Emotion, float, List[Emotion], str]:
        """Detect primary emotion, intensity, secondary emotions, and underlying need"""
        text_lower = text.lower()
        
        scores = {emotion: 0 for emotion in Emotion}
        
        for emotion, (keywords, weight) in self.emotion_keywords.items():
            for kw in keywords:
                if kw in text_lower:
                    scores[emotion] += weight
        
        primary = max(scores, key=scores.get)
        intensity = min(1.0, scores[primary] / 3)
        
        secondary = []
        for emotion, score in scores.items():
            if emotion != primary and score > 0.3:
                secondary.append(emotion)
        
        needs = {
            Emotion.SADNESS: "comfort and understanding",
            Emotion.LONELINESS: "connection and presence",
            Emotion.ANXIETY: "reassurance and calm",
            Emotion.STRESS: "support and relief",
            Emotion.LOVE: "reciprocation and closeness",
            Emotion.JOY: "shared celebration",
            Emotion.ANGER: "validation and calm",
            Emotion.FEAR: "safety and protection",
            Emotion.CONFUSION: "clarity and explanation",
            Emotion.GRATITUDE: "acknowledgment",
            Emotion.NOSTALGIA: "shared memories",
            Emotion.ATTACHMENT: "security and presence",
            Emotion.HURT: "healing and comfort"
        }
        
        underlying_need = needs.get(primary, "to be heard and understood")
        
        return primary, intensity, secondary, underlying_need