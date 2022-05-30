from ast import List
from flask import Flask, render_template, jsonify
import re
import json
import pandas as pd

app = Flask(__name__)


contact = ["name", "123414", "1999-10-1", "1"]

def readAgenda(names: List):
    agenda = []
    filepath = "data/agenda.csv"

    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if line:
                agenda.append(line.split(',', 4))

    return agenda


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/text_simi")
def text_simi():
    f = open("data/agenda.csv", 'r')
    agenda = []

    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            agenda.append(line.split(',', 2))
    
    return render_template("text_simi.html", test=agenda)

@app.route("/api/get_user/<user>")
def getUser(user):
    for contacto in agenda:
        if (user == contacto[0]):
            x = {
                    "name"   : contacto[0],
                    "number" : contacto[1],
                    "birth"  : contacto[2],
                    "gender" : contacto[3][:1]
                }
            return x

    return jsonify(usuario=user, error="User not found."), 404

@app.route("/api/get_adults/<edad>")
def getAdults(edad):
    adults = []
    for contacto in agenda:
        year = int(contacto[2][:4])
        edad = int(edad)
        if (2022-year < edad):
            var = {
                    "name"   : contacto[0],
                    "number" : contacto[1],
                    "birth"  : contacto[2],
                    "gender" : contacto[3]
                }
                
            adults.append(var)

    return jsonify(adults) if adults else jsonify(edad=edad, error="Age not found."), 404

    
if __name__ == '__main__':
    # Pass by value pass by reference
    agenda = readAgenda()
    
    app.run(debug=True, host='0.0.0.0')