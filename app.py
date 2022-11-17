from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return "Hola mundo"

@app.route("/plantilla")
def archivo():
  return render_template("archivo.html")
