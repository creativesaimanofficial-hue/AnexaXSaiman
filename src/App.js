import React, { useState, useEffect } from 'react'; 
import axios from 'axios'; 
import Chat from './components/Chat'; 
import StatusCard from './components/StatusCard'; 
import MemoryPanel from './components/MemoryPanel'; 
import FeaturesPanel from './components/FeaturesPanel'; 
import './App.css'; 
 
function App() { 
    const [status, setStatus] = useState({ 
        love_score: 50, 
        trust_score: 60, 
        understanding_score: 70, 
        total_chats: 0, 
        days_together: 0, 
        stage: 'friendly', 
        mode: 'girlfriend' 
    }); 
    const [memories, setMemories] = useState({ likes: [], dreams: [] }); 
    const [loading, setLoading] = useState(true); 
 
    useEffect(() =
        fetchStatus(); 
        fetchMemories(); 
        const interval = setInterval(fetchStatus, 30000); 
        return () =
    }, []); 
 
    const fetchStatus = async () =
        try { 
            const response = await axios.get('/api/status'); 
            setStatus(response.data); 
        } catch (error) { 
            console.error('Error fetching status:', error); 
        } 
    }; 
 
    const fetchMemories = async () =
        try { 
            const response = await axios.get('/api/memories'); 
            setMemories(response.data); 
        } catch (error) { 
            console.error('Error fetching memories:', error); 
        } finally { 
            setLoading(false); 
        } 
    }; 
 
    const updateStatus = (newStatus) =
        setStatus(newStatus); 
    }; 
 
    return ( 
        <div className="app"> 
            <div className="app-header"> 
                <div className="logo"> 
                    <span className="logo-icon">??</span> 
                    <span className="logo-text">ANEXA</span> 
                </div> 
                <div className="subtitle">Saiman's AI Girlfriend ??</div> 
            </div> 
 
            <div className="app-container"> 
                <div className="sidebar"> 
                    <StatusCard status={status} /> 
                    <MemoryPanel memories={memories} loading={loading} /> 
                    <FeaturesPanel /> 
                </div> 
 
                <div className="main-content"> 
                    <Chat  
                        onStatusUpdate={updateStatus}  
                        initialStatus={status} 
                    /> 
                </div> 
            </div> 
        </div> 
    ); 
} 
 
export default App; 
