from flask import Flask, jsonify, Response, json, render_template
from random import randint, random

from utils import randomDate, randomNif

app = Flask(__name__)

'''Definition of the client list'''
idClient = 0


client_name = [
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

result_client = [{
    "idClient": "client_"+ str(x),
    "nif": randomNif(),
    "name": client_name[randint(0, 5)],
    "surname": client_surname[randint(0, 5)],
    "address": client_addr[randint(0, 6)] + " n. " + str(randint(0, 50)),
    "loation": client_location[randint(0, 12)],
    "fecha_nac": randomDate("1/1/2015 1:30 PM", "1/1/2017 4:50 AM", random())
}
    for x in range(500)]

product_name =[
        "Apple Watch",
        "Apple Watch 2",
        "IPhone 4",
        "IPhone 4s"
        "IPhone 5",
        "IPhone 5s",
        "Iphone 6",
        "Iphone 6s"
        "Iphone 7",
        "Samsung S4",
        "Samsung S5",
        "Samsung S5",
        "Samsung S6",
        "Samsung S7",
        "Samsung S8",
        "Huawei L1",
        "Huawei L2",
        "Huawei L3",
        "Huawei L4",
        "Huawei L5",
        "Huawei L6",
        "Huawei L7",
        "Huawei L8"
        "IPad",
        "IPad 2",
        "IPad Pro",
        "IPad Air",
        "Apple TV",
        "LG TV 43L500HV",
        "LG TV 44L500HV",
        "LG TV 45L500HV",
        "LG TV 46L500HV",
        "Samsung UE40KU1400",
        "Samsung UE41KU1400",
        "Samsung UE42KU1400",
        "Samsung UE43KU1400",
        "Samsung UE44KU1400",
        "Samsung UE45KU1400",
        "Samsung UE46KU1400",
        "Pulseras iWhatch",
        "Pulseras GEAR",
        "AirPods",
        "Cargadores Samsung",
        "Cargadores iPhone",
        "Protectores iPhone",
        "Protectores Huawei",
        "Protectores Samsung"
    ]

product_category = [
        "Smartwatch",
        "Smartphone",
        "Tablets",
        "Smart TV",
        "Whatch Gadges",
        "Chargers",
        "Mobile Gadges"
    ]


result_product = [{
        "idProduct": "Product_"+ str(x),
        "productName": product_name [x],
        "productCategory": product_category [randint(0,5)]
    }
        for x in range(43)]

result_sales =[
    {
        "idSales": "Sale_"+str(x),
        "client": result_client[randint(0,499)]["name"] + " "+ result_client[randint(0,499)]["surname"],
        "product": result_product[randint(0,42)]["productName"],
        "quantity": randint(1,12)
    }
    for x in range(500)]

@app.route('/')
def hello_world():
    return render_template('hello.html', name="Jinja")

@app.route ('/api/v1/clients')
def get_clients():
    return Response(json.dumps(result_client),  mimetype='application/json')

@app.route ('/api/v1/products')
def get_products ():
    return Response(json.dumps(result_product),  mimetype='application/json')

@app.route ('/api/v1/sales')
def get_sales ():
    return Response(json.dumps(result_sales),  mimetype='application/json')

if __name__ == '__main__':
    app.run()
