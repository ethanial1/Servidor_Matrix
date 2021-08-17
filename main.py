from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handleMessage(msg):
    print("Mensaje: ",msg)
    send(msg, broadcast = True)

if __name__ == '__main__':
    socketio.run(app, logger=True, engineio_logger=True)  