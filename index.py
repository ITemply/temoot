import os, json, requests, hashlib, re, cryptography, pytz, random, time, string, logging

from flask import Flask, request, render_template, redirect, abort, url_for, session, copy_current_request_context
from cryptography.fernet import Fernet
from flask_socketio import SocketIO, emit, join_room, leave_room, close_room, rooms, disconnect, send
from threading import Lock
from datetime import datetime

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
app = Flask(__name__)
socketio = SocketIO(app)
thread = None
thread_lock = Lock()

from dotenv import load_dotenv
load_dotenv()

enKey = os.environ['EN_KEY']

@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'GET':
    return render_template('index.html')
  elif request.method == 'POST':
    return '{"response": "Post"}'
  else:
    return '{"response": "Request Method Not Supported"}'

if __name__ == '__main__':
  socketio.run(app, host='0.0.0.0', port=3000, allow_unsafe_werkzeug=True)
