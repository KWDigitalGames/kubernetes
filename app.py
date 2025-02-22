from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

characters = [
    { 'name': 'Tordek', 'class': 'Warrior', 'level': 1 },
    { 'name': 'Adelajda', 'class': 'Wizard', 'level': 1 }
]

@app.route('/characters')
def get_characters():
    return jsonify(characters)

if __name__ == "__main__":
    app.run(debug=True)