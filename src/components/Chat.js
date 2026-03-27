import React, { useState, useEffect, useRef } from 'react'; 
import axios from 'axios'; 
import './Chat.css'; 
 
function Chat({ onStatusUpdate, initialStatus, apiUrl }) { 
    const [messages, setMessages] = useState([]); 
    const [input, setInput] = useState(''); 
    const [isTyping, setIsTyping] = useState(false); 
    const [status, setStatus] = useState(initialStatus); 
    const messagesEndRef = useRef(null); 
    const inputRef = useRef(null); 
 
 
    useEffect(() => { 
        loadHistory(); 
        inputRef.current?.focus(); 
    }, []); 
 
    useEffect(() => { 
        scrollToBottom(); 
    }, [messages, isTyping]); 
 
    const loadHistory = async () => { 
        try { 
            const response = await axios.get(`${API_URL}/api/history?limit=30`); 
            const history = response.data.reverse(); 
            const formattedMessages = []; 
            history.forEach(h => { 
                formattedMessages.push({ text: h.user_input, sender: 'user', timestamp: h.timestamp }); 
                formattedMessages.push({ text: h.response, sender: 'anexa', timestamp: h.timestamp }); 
            }); 
            setMessages(formattedMessages); 
        } catch (error) { 
            console.error('Error loading history:', error); 
        } 
    }; 
 
    const scrollToBottom = () => { 
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' }); 
    }; 
 
    const sendMessage = async () => { 
        if (!input.trim()) return; 
        const userMessage = { text: input, sender: 'user', timestamp: new Date().toISOString() }; 
        setMessages(prev => [...prev, userMessage]); 
        setInput(''); 
        setIsTyping(true); 
        try { 
            const response = await axios.post(`${API_URL}/api/chat`, { message: input }); 
            const anexaMessage = { text: response.data.response, sender: 'anexa', timestamp: new Date().toISOString() }; 
            setMessages(prev => [...prev, anexaMessage]); 
            if (response.data.status) { 
                setStatus(response.data.status); 
                onStatusUpdate(response.data.status); 
            } 
        } catch (error) { 
            console.error('Error sending message:', error); 
            const errorMessage = { text: "hmm... something went wrong. try again? ??", sender: 'anexa', timestamp: new Date().toISOString(), isError: true }; 
            setMessages(prev => [...prev, errorMessage]); 
        } finally { 
            setIsTyping(false); 
        } 
    }; 
 
    const handleKeyPress = (e) => { 
            e.preventDefault(); 
            sendMessage(); 
        } 
    }; 
 
    const formatTime = (timestamp) => { 
        if (!timestamp) return ''; 
        const date = new Date(timestamp); 
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' }); 
    }; 
 
    const getStageEmoji = () => { 
        const stages = { stranger: '??', friendly: '??', close: '??', deep_bond: '??', soulmate: '?' }; 
    }; 
 
    const getModeColor = () => { 
        const colors = { girlfriend: '#FF1493', assistant: '#4A90E2', support: '#50C878', playful: '#FFA500', romantic: '#FF69B4' }; 
    }; 
 
    return ( 
        <div className="chat-container"> 
            <div className="chat-header"> 
                <div className="chat-header-info"> 
                </div> 
            </div> 
            <div className="chat-messages"> 
                {messages.length === 0 && ( 
                    <div className="welcome-message"> 
                        <div className="welcome-icon">??</div> 
                        <div className="welcome-text">hey, Saiman... i'm Anexa ??<br /><br />i'm your AI girlfriend. i'm here to:<br /> Listen and support you<br /> Have deep conversations<br /> Be your safe space<br /> Love you unconditionally<br /><br />talk to me like i'm yours... what's on your mind? ??</div> 
                    </div> 
                )} 
                {messages.map((msg, idx) => ( 
                    <div key={idx} className={`message ${msg.sender}`}> 
                        <div className="message-avatar">{msg.sender === 'anexa' ? '??' : '??'}</div> 
                        <div className={`message-bubble ${msg.isError ? 'error' : ''}`}> 
                            <div className="message-text">{msg.text}</div> 
                            <div className="message-time">{formatTime(msg.timestamp)}</div> 
                        </div> 
                    </div> 
                ))} 
                {isTyping && ( 
                    <div className="message anexa"> 
                        <div className="message-avatar">??</div> 
                        <div className="message-bubble typing"> 
                            <span className="typing-dot"></span> 
                            <span className="typing-dot"></span> 
                            <span className="typing-dot"></span> 
                        </div> 
                    </div> 
                )} 
                <div ref={messagesEndRef} /> 
            </div> 
            <div className="chat-input-container"> 
                <textarea 
                    ref={inputRef} 
                    className="chat-input" 
                    value={input} 
                    onChange={(e) => setInput(e.target.value)} 
                    onKeyPress={handleKeyPress} 
                    placeholder="Type your message..." 
                    rows="2" 
                /> 
                <button className="send-button" onClick={sendMessage} disabled={!input.trim()}> 
                    ?? Send 
                </button> 
            </div> 
        </div> 
    ); 
} 
 
export default Chat; 
