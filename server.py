from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

# app = Flask(__name__)
# socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/log_endpoint', methods=['POST'])
def receive_logs():
    try:
        logs = request.form.get('logs')
       
        # Broadcast the logs to all connected clients via WebSocket
        socketio.emit('log_message', {'logs': logs})

        return 'Logs received successfully', 200
    except Exception as e:
        print(f'Error processing logs: {e}')
        return 'Error processing logs', 500

if __name__ == '__main__':
    socketio.run(app, debug=True, port=8000) 
