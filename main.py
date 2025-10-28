from flask import Flask

app = Flask(__name__)

@app.route("/hello_world")
def hello_world():
    return "<p>Hello, World! Second sentence</p>"

app.run(debug=True)