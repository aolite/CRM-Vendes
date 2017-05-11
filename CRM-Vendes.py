from flask import Flask, jsonify, Response, json, render_template
from random import randint, random

from utils import randomDate, randomNif, alignmentProductCategory

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

client_type = [
    {"idClientType": "clientType_1", "name": "Personal", "description": "Personal/Client accounts"},
    {"idClientType": "clientType_2", "name": "Company", "description": "Personal/Client accounts"}
]

result_client = [{
    "idClient": "client_"+ str(x),
    "nif": randomNif(),
    "name": client_name[randint(0, 5)],
    "surname": client_surname[randint(0, 5)],
    "clientType": client_type[randint(0, 1)]["idClientType"]
} for x in range(500)]

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
        "Huawei L8",
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
        "Watch Gadges",
        "Phone Gadges"
    ]

product_category_desc =[
    "Categories for the smartwhatch",
    "Categories for the smartphones",
    "Categories for the Tablets",
    "Categories for the Smart TVs",
    "Categories for the Watch Gadges",
    "Categories for the Phone Gadges"
]


result_product = [{
        "ProductCode": "Product_"+ str(x),
        "productName": product_name [x],
        "price": randint(300,3000),
        "productCategory": alignmentProductCategory(x, product_category)
    } for x in range(45)]

result_category=[{
    "idCategory": "Category_"+ str(x),
    "categoryName": product_category[x],
    "categoryDesc": product_category_desc[x]
    } for x in range (6)]

result_sales =[
    {
        "idSales": "Sale_"+str(x),
        "client": result_client[randint(0,499)]["nif"],
        "product": result_product[randint(0,42)]["ProductCode"],
        "quantity": randint(1,12),
        "saleDate": randomDate("1/1/2015 1:30 PM", "1/1/2017 4:50 AM", random())
    }
    for x in range(500)]

@app.route('/')
def landing_page():
    return render_template('hello.html')

@app.route('/api')
def api_page():
    return render_template('api.html')

@app.route ('/api/v1/clients')
def get_clients():
    return Response(json.dumps(result_client),  mimetype='application/json')

@app.route ('/api/v1/clientTypes')
def get_clientTypes():
    return Response(json.dumps(client_type),  mimetype='application/json')

@app.route ('/api/v1/products')
def get_products ():
    return Response(json.dumps(result_product),  mimetype='application/json')

@app.route ('/api/v1/categories')
def get_categories ():
    return Response(json.dumps(result_category),  mimetype='application/json')

@app.route ('/api/v1/sales')
def get_sales ():
    return Response(json.dumps(result_sales),  mimetype='application/json')

if __name__ == '__main__':
    app.run()
