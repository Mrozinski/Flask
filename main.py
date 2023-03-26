from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
from dane import pobierz_dane
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dodaj")
def dodaj():
    dane = request.args.get('dane', None)
    return f"Dodaje ... {dane}"

@app.route("/danefirmy", methods=["POST", "GET"])
def danefirmy():
    nip = request.args.get('nip', None)
    dane = pobierz_dane(nip)
    if request.method=="POST":
       return redirect(url_for("dodaj", dane=dane))
    else:
       return render_template("danef.html", dane=dane, d = datetime.today().strftime('%Y-%m-%d'))

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        return redirect(url_for("danefirmy", nip=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>{usr}</h1>"

if __name__ == "__main__":
    app.run(debug=True)