from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def hello_world():
  print("Hello World!")
  return "Hello, World!"

incomes = [
  { 'description': 'salary', 'amount': 50000 }
]


@app.route('/incomes')
def get_incomes():
  print("getting incomes",incomes)
  return jsonify(incomes)


@app.route('/incomes', methods=['POST'])
def add_income():
  incomes.append(request.get_json())
  return '', 204

if __name__ == "__main__":
    app.run(debug=True)