from flask import Flask, jsonify, request
from flask_cors import CORS
import yfinance as yf

app = Flask(__name__)
CORS(app)

@app.route('/welcome', methods=['GET'])
def get_data():
    data = {"message": "Hello, World!"}
    return jsonify(data)

@app.route('/api/stock', methods=['GET'])
def get_stock():
    ticker = request.args.get('ticker')
    stock = yf.Ticker(ticker)
    data = stock.info
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True, port=5005)
