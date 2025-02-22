import os
from flask import Flask, render_template_string
from datetime import datetime

app = Flask(__name__)

log_directory = os.getenv("LOG_DIR")
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

@app.route('/')
def index():
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Create a log line and write it to the file in the mounted volume
    log_line = f"Accessed at {timestamp}\n"
    log_file_path = os.path.join(log_directory, 'access.log')
    
    with open(log_file_path, 'a') as log_file:
        log_file.write(log_line)

    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Current Timestamp</title>
        </head>
        <body>
            <h1>Current Timestamp</h1>
            <p>The current timestamp is: {timestamp}</p>
            <p>Written to: {log_file_path}</p>
        </body>
    </html>
    """
    return render_template_string(html)

if __name__ == '__main__':
    app.run(debug=True)
