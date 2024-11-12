from flask import Flask
import os
import datetime
import pytz
import subprocess

app = Flask(__name__)

def get_username():
    try:
        return os.getlogin()
    except OSError:
        return os.environ.get('USER') or os.environ.get('USERNAME') or "Unknown User"

@app.route('/htop')
def htop():
    
    name = "Aditya Kshatariya"
    
    
    username = get_username()
    
    
    ist_timezone = pytz.timezone("Asia/Kolkata")
    server_time = datetime.datetime.now(ist_timezone).strftime("%Y-%m-%d %H:%M:%S")
    
    
    top_output = subprocess.check_output("top -bn1 | head -n 10", shell=True).decode("utf-8")
    
    
    html_content = f"""
    <html>
    <head><title>/htop</title></head>
    <body>
        <h1>/htop Endpoint</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time in IST:</strong> {server_time}</p>
        <pre><strong>Top Output:</strong><br>{top_output}</pre>
    </body>
    </html>
    """
    return html_content

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
