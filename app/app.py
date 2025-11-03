from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Trabalho Final CI/CD Pipelines - 21/11/2025"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
