from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
  return " estoy en archivo"

@app.route("/archivo")
def archivo():
  return render_template("archivo.html")

@app.route("/lista")
def lista():
    numeros=[1,2,3,4]
    return render_template("lista.html", lista=numeros)