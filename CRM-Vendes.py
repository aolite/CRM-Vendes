from flask import Flask, jsonify, Response, json
from random import randint, random

from utils import randomDate, randomNif

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify( 'Hello World!');

@app.route ('/api/v1/clients')
def get_clients():
    idClient =0;

    client_name =[
        "David",
        "Alex",
        "Mark",
        "Maria",
        "Julien",
        "Sophia"
    ]
    client_surname = [
        "Smith",
        "Black",
        "Felon",
        "Garcia",
        "Ho",
        "Dark"
    ]

    client_addr = [
        "Av. del Olmo",
        "Av. st Patrick station",
        "Central road",
        "Calle del Cerco",
        "Av. Wall Street",
        "Calle del ultimo trago",
        "Av. St John"
    ]

    client_location = [
        "Spain",
        "Argentina",
        "England",
        "Germany",
        "Brazil",
        "US",
        "China",
        "India",
        "Japan",
        "Mexico",
        "France",
        "Italy",
        "Russia"
    ]

    result=[{
        "idClient": idClient+1,
        "nif": randomNif (),
        "name": client_name[randint(0,5)],
        "surname": client_surname [randint(0,5)],
        "address": client_addr [randint(0,6)] + " n. "+ str(randint(0,50)),
        "loation": client_location [randint(0,12)],
        "fecha_nac": randomDate("1/1/2005 1:30 PM", "1/1/2009 4:50 AM", random())
        }
            for x in range (500) ]

    return Response(json.dumps(result),  mimetype='application/json')


if __name__ == '__main__':
    app.run()
