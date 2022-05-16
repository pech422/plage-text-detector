from flask import Flask, render_template, jsonify
import re
import json

app = Flask(__name__)


def readAgenda():
    agenda = []
    filepath = "data/agenda.csv"
    with open(filepath, 'r') as fp:
        line = fp.readline()
        while line:
            line = fp.readline()
            agenda.append(line.split(',', 2))

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
                    "number" : contacto[1]
                }

            return x


    return jsonify(usuario=user, error="User not found."), 404


if __name__ == '__main__':
    # Pass by value pass by reference
    agenda = readAgenda()
    
    app.run(debug=True, host='0.0.0.0')