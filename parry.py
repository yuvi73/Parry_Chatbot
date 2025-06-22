import random
import re

class Parry:
    class State:
        NEUTRAL = 'neutral'
        SUSPICIOUS = 'suspicious'
        ANGRY = 'angry'
        FEARFUL = 'fearful'
        DEFENSIVE = 'defensive'

    def __init__(self):
        self.state = self.State.NEUTRAL
        self.responses = self._init_responses()
        self.triggers = self._init_triggers()

    def _init_responses(self):
        return {
            'greeting': [
                "Hello there.", "Hi.", "Hello.", "Good day."
            ],
            'how_are_you': [
                "I'm okay, I guess.", "Fine, thanks for asking.", "I'm doing alright.", "Could be better."
            ],
            'name': [
                "My name is Parry.", "I'm Parry.", "They call me Parry.", "Parry is my name."
            ],
            'suspicious': [
                "Why are you asking me that?", "What do you want to know that for?", "Are you trying to trick me?", "I don't trust you.", "What's your angle here?"
            ],
            'angry': [
                "I don't like your tone!", "You're making me angry!", "Stop bothering me!", "I've had enough of this!", "Leave me alone!"
            ],
            'fearful': [
                "I'm scared.", "Please don't hurt me.", "I don't want any trouble.", "Leave me be.", "I'm afraid."
            ],
            'defensive': [
                "I didn't do anything wrong!", "You can't prove anything!", "I'm innocent!", "Don't accuse me!", "I haven't done anything!"
            ],
            'default': [
                "I don't understand.", "What do you mean?", "Can you explain that?", "I'm not sure what you're saying.", "Hmm."
            ]
        }

    def _init_triggers(self):
        return {
            'police': self.State.FEARFUL,
            'doctor': self.State.SUSPICIOUS,
            'hospital': self.State.FEARFUL,
            'medication': self.State.DEFENSIVE,
            'treatment': self.State.DEFENSIVE,
            'crazy': self.State.ANGRY,
            'insane': self.State.ANGRY,
            'mental': self.State.SUSPICIOUS,
            'why': self.State.SUSPICIOUS,
            'how': self.State.SUSPICIOUS,
            'what': self.State.SUSPICIOUS,
            'when': self.State.SUSPICIOUS,
            'where': self.State.SUSPICIOUS,
            'who': self.State.SUSPICIOUS,
        }

    def respond(self, user_input):
        text = user_input.lower()
        # State-changing triggers
        for trigger, state in self.triggers.items():
            if re.search(r'\b' + re.escape(trigger) + r'\b', text):
                self.state = state
                break
        # Pattern-based responses
        if any(greet in text for greet in ['hello', 'hi', 'hey']):
            response = random.choice(self.responses['greeting'])
        elif 'how are you' in text or 'how do you feel' in text:
            response = random.choice(self.responses['how_are_you'])
        elif 'name' in text or 'who are you' in text:
            response = random.choice(self.responses['name'])
        else:
            if self.state == self.State.SUSPICIOUS:
                response = random.choice(self.responses['suspicious'])
            elif self.state == self.State.ANGRY:
                response = random.choice(self.responses['angry'])
            elif self.state == self.State.FEARFUL:
                response = random.choice(self.responses['fearful'])
            elif self.state == self.State.DEFENSIVE:
                response = random.choice(self.responses['defensive'])
            else:
                response = random.choice(self.responses['default'])
        # Gradually return to neutral
        if self.state != self.State.NEUTRAL and random.random() < 0.3:
            self.state = self.State.NEUTRAL
        return response, self.state 