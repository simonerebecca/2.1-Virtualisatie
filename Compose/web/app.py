from flask import Flask
import os, redis

app = Flask(__name__)
r = redis.Redis(host=os.getenv("REDIS_HOST","redis"), port=6379)

@app.route("/")
def index():
    visits = r.incr("visits")
    return f"""
    <html>
    <head>
        <title>Simone’s Pink WebApp</title>
        <style>
            body {{
                background-color: #ffe6f2;
                color: #cc0066;
                font-family: Arial, sans-serif;
                text-align: center;
                margin-top: 10%;
            }}
            h1 {{
                font-size: 3em;
            }}
            p {{
                font-size: 1.5em;
            }}
        </style>
    </head>
    <body>
        <h1> Dit is de WebApp van Simone </h1>
        <p>Studentnummer: 494729</p>
        <p>Deze app draait in een Docker Compose omgeving met Redis.</p>
    </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
