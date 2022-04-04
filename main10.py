from flask import Flask, request
from flask_cors import CORS, cross_origin
from optimalization_algorithm.main import optimal_currency_exchange

app = Flask(__name__)
cors = CORS(app)

import json

@app.route('/targetcurrencies', methods=['POST'])
@cross_origin()
def target_currencies():
    data = {
        "BNB": ["SOL", "ADA", "XRP", "LUNA", "DOT", "AVAX", "MATIC"],
        "BTC": ["ETH", "BNB", "SOL", "ADA", "XRP", "LUNA", "DOT", "DOGE", "AVAX", "MATIC"],
        "ETH": ["BNB", "SOL", "ADA", "XRP", "LUNA", "DOT", "AVAX", "MATIC"],
        "EUR": ["BTC", "ETH", "BNB", "SOL", "ADA", "XRP", "LUNA", "DOT", "DOGE", "AVAX", "MATIC"],
        "USDF": ["EUR", "BTC", "ETH", "BNB", "SOL", "ADA", "XRP", "LUNA", "DOT", "DOGE", "AVAX", "MATIC"]
    }
    request_data = request.get_json()

    first = request_data["first"]
    s = []
    for key in data:
        if key == first:
            s = data[key]
    return_data: json = json.dumps(s)
    return return_data


@app.route('/currencies')
@cross_origin()
def currencies():
    data12: json = json.dumps(["BTC", "BNB", "ETH", "USDT", "EUR"])
    return data12


@app.route('/sequence', methods=['POST'])
@cross_origin()
def sequence():
    request_data = request.get_json()
    first = request_data['first']
    second = request_data['second']
    amount = request_data['amount']
    data1: json = json.dumps(optimal_currency_exchange(amount, first, second))
    return data1


app.run(port=5000)
