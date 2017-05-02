from flask import Flask, jsonify, Response, json
from random import randint

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

    client_country = [
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
        "name": client_name[randint(0,5)],
        "surname": client_surname [randint(0,5)],
        "address": client_addr [randint(0,6)] + " n. "+ str(randint(0,50)),
        "loation": client_country [randint(0,12)]
        }
            for x in range (500) ]

    return Response(json.dumps(result),  mimetype='application/json')


if __name__ == '__main__':
    app.run()
