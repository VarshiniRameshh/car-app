from flask import Flask, jsonify

app = Flask(__name__)

# Sample car data
cars = [
    {"id": 1, "name": "Model S", "manufacturer": "Tesla", "year": 2023},
    {"id": 2, "name": "Mustang", "manufacturer": "Ford", "year": 2022}
]

@app.route('/')
def home():
    return "Welcome to the Car Info App!"

@app.route('/cars', methods=['GET'])
def get_cars():
    return jsonify(cars)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)