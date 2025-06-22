from flask import Flask, render_template, request, jsonify, send_from_directory
from parry_advanced import AdvancedParry
import os
import random

app = Flask(__name__)
parry_bot = AdvancedParry()

# Sound effects mapping
SOUND_EFFECTS = {
    'neutral': ['neutral1.mp3', 'neutral2.mp3'],
    'suspicious': ['suspicious1.mp3', 'suspicious2.mp3'],
    'angry': ['angry1.mp3', 'angry2.mp3'],
    'fearful': ['fearful1.mp3', 'fearful2.mp3'],
    'defensive': ['defensive1.mp3', 'defensive2.mp3'],
    'paranoid': ['paranoid1.mp3', 'paranoid2.mp3'],
    'delusional': ['delusional1.mp3', 'delusional2.mp3'],
    'persecuted': ['persecuted1.mp3', 'persecuted2.mp3']
}

@app.route('/')
def index():
    return render_template('index_advanced.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    response, state, paranoia_level = parry_bot.respond(user_input)
    
    # Select appropriate sound effect
    sound_effect = random.choice(SOUND_EFFECTS.get(state, SOUND_EFFECTS['neutral']))
    
    return jsonify({
        'response': response, 
        'state': state, 
        'paranoia_level': paranoia_level,
        'sound_effect': sound_effect
    })

@app.route('/static/sounds/<filename>')
def serve_sound(filename):
    return send_from_directory('static/sounds', filename)

@app.route('/static/backgrounds/<filename>')
def serve_background(filename):
    return send_from_directory('static/backgrounds', filename)

if __name__ == '__main__':
    app.run(debug=True) 