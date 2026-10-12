from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>🚀 DevOps Mini Project</h1>
    <h2>Dockerized Web Application</h2>
    <p>Application is running successfully!</p>
    <p>Environment: Docker</p>
    <p>Status: Healthy</p>
    """

@app.route("/health")
def health():
    return {
        "status": "healthy",
        "application": "dockerized-web-app"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
