from flask import Flask
app = Flask(__name__)

@app.route('/')
def yolo():
    return 'yolo'