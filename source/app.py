from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Gunicorn on Minikube!\n"

@app.get("/healthz")
def health():
    return "ok", 200
