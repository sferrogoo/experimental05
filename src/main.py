import os
from flask import Flask, render_template

# Transpile the Python code to JavaScript
os.system("transcrypt -b -n src/three_app.py")
os.system("cp src/__target__/three_app.js static/js/three_app.js")


app = Flask(__name__, template_folder='../templates', static_folder='../static')

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
