from flask import Flask, render_template, jsonify
import re
import json
import pandas as pd
from Contact import Contact

app = Flask(__name__)


contact1 = Contact("Cheri Batson","06243158218-21","1977-1-19","1")

def readAgenda():
    agenda = []
    filepath = "data/agenda.csv"

    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            if line:
                aux = line.split(',', 4)
                agenda.append(Contact(aux[0],aux[1],aux[2],aux[3]))

    return agenda


@app.route("/")
def index():
    return render_template("index.html")


contactos = []

@app.route("/text_simi")
def text_simi():
    for i in range(len(agenda)):
        contactos.append(agenda[i].to_json())

    return jsonify(contactos)

@app.route("/api/get_user/<user>")
def getUser(user):
    for i in range(len(agenda)):
        name = agenda[i].getName()
        if (user == name):
            return agenda[i].to_json()

    return jsonify(usuario=user, error="User not found."), 404

@app.route("/api/get_adults/<edad>")
def getAdults(edad):
    adults = []
    for contact in agenda:
        if (contact.isAdult(edad)):
            adults.append(contact.to_json())


    return jsonify(adults) if adults else jsonify(edad=edad, error="Age not found."), 404

    
if __name__ == '__main__':
    # Pass by value pass by reference
    agenda = readAgenda()
    
    app.run(debug=True, host='0.0.0.0')