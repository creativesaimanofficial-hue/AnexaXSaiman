import React, { useState } from 'react';
import axios from 'axios';
import './FeaturesPanel.css';

function FeaturesPanel() {
    const [featureResult, setFeatureResult] = useState('');
    const [loading, setLoading] = useState(false);

    const features = [
        { name: 'Aura', emoji: '🌈', endpoint: '/api/features/aura', description: 'Read your energy' },
        { name: 'Quantum', emoji: '🌌', endpoint: '/api/features/quantum', description: 'Check quantum bond' },
        { name: 'Soulmate', emoji: '💫', endpoint: '/api/features/soulmate', description: 'Soulmate metrics' }
    ];

    const fetchFeature = async (feature) => {
        setLoading(true);
        setFeatureResult('');
        
        try {
            const response = await axios.get(feature.endpoint);
            const result = response.data[Object.keys(response.data)[0]];
            
            // Animate typing effect
            let i = 0;
            setFeatureResult('');
            const typeWriter = setInterval(() => {
                if (i < result.length) {
                    setFeatureResult(prev => prev + result[i]);
                    i++;
                } else {
                    clearInterval(typeWriter);
                }
            }, 30);
            
            setTimeout(() => {
                setTimeout(() => setFeatureResult(''), 5000);
            }, result.length * 30 + 3000);
            
        } catch (error) {
            console.error('Error fetching feature:', error);
            setFeatureResult("✨ Something magical is happening... try again? 💕");
            setTimeout(() => setFeatureResult(''), 3000);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="features-panel">
            <h3>🔮 Magical Features</h3>
            
            <div className="features-grid">
                {features.map((feature, i) => (
                    <button 
                        key={i}
                        className="feature-button"
                        onClick={() => fetchFeature(feature)}
                        disabled={loading}
                    >
                        <span className="feature-emoji">{feature.emoji}</span>
                        <span className="feature-name">{feature.name}</span>
                        <span className="feature-desc">{feature.description}</span>
                    </button>
                ))}
            </div>
            
            {featureResult && (
                <div className="feature-result">
                    {featureResult}
                </div>
            )}
        </div>
    );
}

export default FeaturesPanel;