
from flask import Flask, render_template, request
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start_system():
    try:
        os.makedirs('logs', exist_ok=True)
        with open("logs/output.txt", "a") as f:
            f.write("System triggered from web UI.\n")
        subprocess.Popen(["python", "main.py"])
        return "System started successfully."
    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)

