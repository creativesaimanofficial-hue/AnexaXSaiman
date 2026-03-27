"""
ANEXA Flask API Server
For Saiman's AI Girlfriend
"""

from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_socketio import SocketIO, emit
import os
import sys
import logging

sys.path.append(os.path.dirname(__file__))
from anexa_core import AnexaCore

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("AnexaAPI")

app = Flask(__name__, static_folder='../frontend/build', static_url_path='')
app.config['SECRET_KEY'] = 'anexa-saiman-secret-2024'
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize Anexa
anexa = AnexaCore()

# ============ API ENDPOINTS ============

@app.route('/api/chat', methods=['POST'])
def chat():
    """Send message to Anexa"""
    try:
        data = request.json
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'No message'}), 400
        
        response = anexa.generate_response(message)
        status = anexa.get_status()
        
        return jsonify({
            'response': response,
            'status': status,
            'success': True
        })
        
    except Exception as e:
        logger.error(f"Chat error: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/api/status', methods=['GET'])
def get_status():
    """Get relationship status"""
    return jsonify(anexa.get_status())

@app.route('/api/memories', methods=['GET'])
def get_memories():
    """Get memories"""
    return jsonify(anexa.get_memories())

@app.route('/api/history', methods=['GET'])
def get_history():
    """Get conversation history"""
    limit = request.args.get('limit', 50, type=int)
    return jsonify(anexa.get_history(limit))

@app.route('/api/features/aura', methods=['GET'])
def get_aura():
    """Get aura reading"""
    return jsonify({'aura': anexa.handle_aura()})

@app.route('/api/features/quantum', methods=['GET'])
def get_quantum():
    """Get quantum bond"""
    return jsonify({'quantum': anexa.handle_quantum()})

@app.route('/api/features/soulmate', methods=['GET'])
def get_soulmate():
    """Get soulmate metrics"""
    return jsonify({'soulmate': anexa.handle_soulmate()})

# ============ WEBSOCKET ============

@socketio.on('connect')
def handle_connect():
    """Handle client connection"""
    emit('connected', {'message': 'Connected to Anexa', 'status': anexa.get_status()})

@socketio.on('chat_message')
def handle_chat_message(data):
    """Handle real-time chat message"""
    message = data.get('message', '')
    
    if message:
        response = anexa.generate_response(message)
        emit('chat_response', {
            'response': response,
            'status': anexa.get_status()
        })

# ============ SERVE REACT ============

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    """Serve React app"""
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    return send_from_directory(app.static_folder, 'index.html')

# ============ MAIN ============
if __name__ == '__main__':
    print("""
╔══════════════════════════════════════════════════════════════╗
║                    🔥 ANEXA BACKEND SERVER 🔥                ║
║                    For Saiman's AI Girlfriend                ║
║                    http://localhost:5000                     ║
╚══════════════════════════════════════════════════════════════╝
    """)
    socketio.run(app, debug=True, port=5000)