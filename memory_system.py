"""
Advanced Memory System with SQLite
Stores likes, dislikes, dreams, goals, emotional memories
"""

import sqlite3
import json
import time
from datetime import datetime
from typing import Dict, List, Optional, Any
import logging

logger = logging.getLogger("MemorySystem")

class MemorySystem:
    """Persistent memory storage with importance scoring"""
    
    def __init__(self, db_path: str = "saiman_memory.db"):
        self.db_path = db_path
        self.init_database()
    
    def init_database(self):
        """Initialize database tables"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id TEXT PRIMARY KEY,
                name TEXT,
                created_at TEXT
            )
        ''')
        
        # Memories table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS memories (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                type TEXT,
                content TEXT,
                importance REAL,
                emotion TEXT,
                timestamp TEXT
            )
        ''')
        
        # Relationship table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS relationship (
                user_id TEXT PRIMARY KEY,
                love_score REAL,
                trust_score REAL,
                understanding_score REAL,
                bond_level INTEGER,
                total_chats INTEGER,
                days_together INTEGER,
                first_meeting TEXT,
                last_interaction TEXT,
                milestones TEXT,
                relationship_stage TEXT
            )
        ''')
        
        # Conversations table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS conversations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                user_input TEXT,
                response TEXT,
                emotion TEXT,
                mode TEXT,
                timestamp TEXT
            )
        ''')
        
        # Emotional history table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS emotional_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id TEXT,
                emotion TEXT,
                intensity REAL,
                context TEXT,
                timestamp TEXT
            )
        ''')
        
        conn.commit()
        conn.close()
        logger.info("Database initialized")
    
    def save_memory(self, user_id: str, mem_type: str, content: str, 
                    importance: float = 0.5, emotion: str = None):
        """Save a memory"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO memories (user_id, type, content, importance, emotion, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, mem_type, content, importance, emotion, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
        logger.info(f"Memory saved: {mem_type} - {content[:50]}")
    
    def get_memories(self, user_id: str, mem_type: str = None, limit: int = 10) -> List[Dict]:
        """Get memories"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        if mem_type:
            cursor.execute('''
                SELECT type, content, importance, timestamp FROM memories
                WHERE user_id = ? AND type = ?
                ORDER BY importance DESC, timestamp DESC LIMIT ?
            ''', (user_id, mem_type, limit))
        else:
            cursor.execute('''
                SELECT type, content, importance, timestamp FROM memories
                WHERE user_id = ?
                ORDER BY importance DESC, timestamp DESC LIMIT ?
            ''', (user_id, limit))
        
        rows = cursor.fetchall()
        conn.close()
        
        return [{"type": r[0], "content": r[1], "importance": r[2], "timestamp": r[3]} for r in rows]
    
    def save_conversation(self, user_id: str, user_input: str, response: str, 
                          emotion: str, mode: str):
        """Save conversation"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO conversations (user_id, user_input, response, emotion, mode, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (user_id, user_input[:500], response[:500], emotion, mode, datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
    
    def save_emotional_event(self, user_id: str, emotion: str, intensity: float, context: str):
        """Save emotional event"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT INTO emotional_history (user_id, emotion, intensity, context, timestamp)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_id, emotion, intensity, context[:200], datetime.now().isoformat()))
        
        conn.commit()
        conn.close()
    
    def get_relationship(self, user_id: str) -> Dict:
        """Get relationship data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('SELECT * FROM relationship WHERE user_id = ?', (user_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return {
                "love_score": row[1],
                "trust_score": row[2],
                "understanding_score": row[3],
                "bond_level": row[4],
                "total_chats": row[5],
                "days_together": row[6],
                "first_meeting": row[7],
                "last_interaction": row[8],
                "milestones": json.loads(row[9]) if row[9] else [],
                "relationship_stage": row[10]
            }
        return None
    
    def save_relationship(self, user_id: str, data: Dict):
        """Save relationship data"""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        
        cursor.execute('''
            INSERT OR REPLACE INTO relationship 
            (user_id, love_score, trust_score, understanding_score, bond_level, 
             total_chats, days_together, first_meeting, last_interaction, milestones, relationship_stage)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            user_id,
            data["love_score"],
            data["trust_score"],
            data["understanding_score"],
            data["bond_level"],
            data["total_chats"],
            data["days_together"],
            data["first_meeting"],
            data["last_interaction"],
            json.dumps(data.get("milestones", [])),
            data.get("relationship_stage", "friendly")
        ))
        
        conn.commit()
        conn.close()