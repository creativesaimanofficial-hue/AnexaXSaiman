import React from 'react';
import './MemoryPanel.css';

function MemoryPanel({ memories, loading }) {
    if (loading) {
        return (
            <div className="memory-panel">
                <h3>💭 I Remember...</h3>
                <div className="loading">Loading memories...</div>
            </div>
        );
    }

    const hasMemories = (memories.likes?.length > 0) || (memories.dreams?.length > 0);

    return (
        <div className="memory-panel">
            <h3>💭 I Remember...</h3>
            
            {memories.likes?.length > 0 && (
                <div className="memory-section">
                    <div className="memory-icon">❤️</div>
                    <div className="memory-content">
                        {memories.likes.slice(-3).map((like, i) => (
                            <div key={i} className="memory-item">you like {like}</div>
                        ))}
                    </div>
                </div>
            )}
            
            {memories.dreams?.length > 0 && (
                <div className="memory-section">
                    <div className="memory-icon">🌟</div>
                    <div className="memory-content">
                        {memories.dreams.slice(-2).map((dream, i) => (
                            <div key={i} className="memory-item">you dream of {dream}</div>
                        ))}
                    </div>
                </div>
            )}
            
            {!hasMemories && (
                <div className="empty-memory">
                    still getting to know you... tell me about yourself 😊
                </div>
            )}
        </div>
    );
}

export default MemoryPanel;