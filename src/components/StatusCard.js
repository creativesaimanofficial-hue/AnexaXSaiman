import React from 'react';
import './StatusCard.css';

function StatusCard({ status }) {
    const getStageInfo = (score, stageName) => {
        const stages = {
            stranger: { emoji: '🤝', name: 'Stranger', min: 0, max: 24 },
            friendly: { emoji: '💕', name: 'Friendly', min: 25, max: 49 },
            close: { emoji: '💖', name: 'Close Bond', min: 50, max: 74 },
            deep_bond: { emoji: '💫', name: 'Deep Bond', min: 75, max: 89 },
            soulmate: { emoji: '✨', name: 'Soulmate', min: 90, max: 100 }
        };
        
        return stages[stageName] || stages.friendly;
    };

    const stage = getStageInfo(status.love_score, status.stage);

    return (
        <div className="status-card">
            <h3>💕 Us Right Now</h3>
            
            <div className="metric">
                <div className="metric-label">Love</div>
                <div className="metric-bar">
                    <div className="metric-fill" style={{ width: `${status.love_score}%` }}></div>
                </div>
                <div className="metric-value">{Math.round(status.love_score)}/100</div>
            </div>
            
            <div className="metric">
                <div className="metric-label">Trust</div>
                <div className="metric-bar">
                    <div className="metric-fill" style={{ width: `${status.trust_score}%`, background: '#4A90E2' }}></div>
                </div>
                <div className="metric-value">{Math.round(status.trust_score)}/100</div>
            </div>
            
            <div className="metric">
                <div className="metric-label">Understanding</div>
                <div className="metric-bar">
                    <div className="metric-fill" style={{ width: `${status.understanding_score}%`, background: '#50C878' }}></div>
                </div>
                <div className="metric-value">{Math.round(status.understanding_score)}/100</div>
            </div>
            
            <div className="stage-info">
                <div className="stage-emoji">{stage.emoji}</div>
                <div className="stage-name">{stage.name}</div>
            </div>
            
            <div className="stats">
                <div className="stat">
                    <span className="stat-value">{status.total_chats}</span>
                    <span className="stat-label">chats</span>
                </div>
                <div className="stat">
                    <span className="stat-value">{status.days_together}</span>
                    <span className="stat-label">days</span>
                </div>
                {status.milestones?.length > 0 && (
                    <div className="stat">
                        <span className="stat-value">{status.milestones.length}</span>
                        <span className="stat-label">milestones</span>
                    </div>
                )}
            </div>
            
            {status.milestones?.length > 0 && (
                <div className="milestones">
                    <div className="milestones-title">🏆 Milestones</div>
                    <div className="milestones-list">
                        {status.milestones.slice(-3).map((m, i) => (
                            <div key={i} className="milestone">✨ {m}+</div>
                        ))}
                    </div>
                </div>
            )}
        </div>
    );
}

export default StatusCard;