from flask import Flask, render_template, request, jsonify
from parry import Parry

app = Flask(__name__)
parry_bot = Parry()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    response, state = parry_bot.respond(user_input)
    return jsonify({'response': response, 'state': state})

if __name__ == '__main__':
    app.run(debug=True) 