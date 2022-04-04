from flask import Flask,request
from flask_cors import CORS, cross_origin
from optimalization_algorithm.main import optimal_currency_exchange
import Cryptocurrencies, os
app = Flask(__name__)
cors = CORS(app)

import json

@app.route('/currencies', methods=['GET', 'POST'])
@cross_origin()
def currencies():
    request_data = request.get_json()
    if request.method == 'GET':
        data: json = json.dumps(["BTC", "BNB", "ETH", "USDT", "EUR"])
        return data
    else:
        first = request_data['first']
        arr = next(filter(x.currencies for x in os.listdir(r"./Cryptocurrencies") if x[:-3]==first))
        data: json = json.dumps(arr)
        return data


@app.route('/sequence', methods=['POST'])
@cross_origin()
def sequence():
    request_data = request.get_json()
    first = request_data['first']
    second = request_data['second']
    data: json = json.dumps(optimal_currency_exchange(first, second))
    return data


app.run(port=5000)