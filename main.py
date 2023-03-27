from flask import Flask, redirect, url_for, render_template, request
import pandas as pd
from dane import pobierz_dane
from dane import dodaj_kon
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dodaj")
def dodaj():
    dane = []
    nazwa = request.args.get('nazwa', None)
    dane.append(nazwa)
    nip = request.args.get('nip', None)
    dane.append(nip)
    regon = nip = request.args.get('regon', None)
    dane.append(regon)
    gmina = request.args.get('gmina', None)
    dane.append(gmina)
    miejscowosc = request.args.get('miejscowosc', None)
    dane.append(miejscowosc)
    kod = request.args.get('kod', None)
    dane.append(kod)
    ulica = request.args.get('ulica', None)
    dane.append(ulica)
    numer = request.args.get('numer', None)
    dane.append(numer)
    data = request.args.get('data', None)
    dodaj_kon(dane)
    return f"Dodaje ... {nazwa}, {nip}, {regon}, {miejscowosc}, {ulica}, {numer}, {data}"

@app.route("/danefirmy", methods=["POST", "GET"])
def danefirmy():
    nip = request.args.get('nip', None)
    dane = pobierz_dane(nip)
    if request.method=="POST":
       data = request.form["d"]
       return redirect(url_for("dodaj", nazwa=dane['Nazwa'], nip=dane['Nip'], regon= dane['Regon'], gmina=dane['Gmina'], miejscowosc=dane['Miejscowosc'], kod=dane['KodPocztowy'], ulica=dane['Ulica'], numer=dane['NrNieruchomosci'],data=data))
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