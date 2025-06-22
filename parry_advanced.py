import random
import re
import json
from collections import defaultdict
import nltk
from textblob import TextBlob
import spacy

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

class AdvancedParry:
    class State:
        NEUTRAL = 'neutral'
        SUSPICIOUS = 'suspicious'
        ANGRY = 'angry'
        FEARFUL = 'fearful'
        DEFENSIVE = 'defensive'
        PARANOID = 'paranoid'
        DELUSIONAL = 'delusional'
        PERSECUTED = 'persecuted'

    def __init__(self):
        self.state = self.State.NEUTRAL
        self.state_history = []
        self.conversation_memory = []
        self.paranoia_level = 0.0  # 0.0 to 1.0
        self.delusional_beliefs = self._init_delusions()
        self.persecutory_themes = self._init_persecutory_themes()
        self.responses = self._init_responses()
        self.triggers = self._init_triggers()
        self.nlp = spacy.load("en_core_web_sm")
        
    def _init_delusions(self):
        return {
            'surveillance': [
                "They're watching me through the walls.",
                "I can hear them listening to my thoughts.",
                "The government has cameras everywhere.",
                "My phone is recording everything I say."
            ],
            'mind_control': [
                "They're controlling my thoughts with radio waves.",
                "I can feel them manipulating my brain.",
                "The voices are coming from satellites.",
                "They're using technology to read my mind."
            ],
            'persecution': [
                "They're following me everywhere.",
                "Everyone is plotting against me.",
                "The doctors are trying to poison me.",
                "They want to lock me up forever."
            ],
            'grandeur': [
                "I'm the only one who can see the truth.",
                "They're afraid of what I know.",
                "I have special powers they don't understand.",
                "I'm the key to everything."
            ]
        }

    def _init_persecutory_themes(self):
        return {
            'authority': ['police', 'government', 'fbi', 'cia', 'agents', 'officials'],
            'medical': ['doctor', 'hospital', 'medication', 'treatment', 'therapy', 'psychiatrist'],
            'technology': ['cameras', 'phones', 'computers', 'internet', 'satellites', 'surveillance'],
            'social': ['neighbors', 'strangers', 'everyone', 'people', 'they', 'them'],
            'personal': ['family', 'friends', 'colleagues', 'boss', 'teacher']
        }

    def _init_responses(self):
        base_responses = {
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
                "Why are you asking me that?", "What do you want to know that for?", 
                "Are you trying to trick me?", "I don't trust you.", "What's your angle here?"
            ],
            'angry': [
                "I don't like your tone!", "You're making me angry!", "Stop bothering me!", 
                "I've had enough of this!", "Leave me alone!"
            ],
            'fearful': [
                "I'm scared.", "Please don't hurt me.", "I don't want any trouble.", 
                "Leave me be.", "I'm afraid."
            ],
            'defensive': [
                "I didn't do anything wrong!", "You can't prove anything!", "I'm innocent!", 
                "Don't accuse me!", "I haven't done anything!"
            ],
            'paranoid': [
                "I know what you're really up to.", "You can't fool me.", 
                "I see through your lies.", "I know the truth.", "You're one of them."
            ],
            'delusional': [
                "The voices told me about you.", "I can see what others can't.", 
                "They're controlling everything.", "I have special knowledge.", 
                "The patterns are clear to me."
            ],
            'persecuted': [
                "You're all against me.", "I'm being targeted.", "They want to destroy me.", 
                "I'm the victim here.", "Everyone is plotting."
            ],
            'default': [
                "I don't understand.", "What do you mean?", "Can you explain that?", 
                "I'm not sure what you're saying.", "Hmm."
            ]
        }
        
        # Add delusional responses
        for delusion_type, responses in self.delusional_beliefs.items():
            base_responses[f'delusional_{delusion_type}'] = responses
            
        return base_responses

    def _init_triggers(self):
        return {
            # Authority triggers
            'police': (self.State.FEARFUL, 0.3),
            'government': (self.State.PARANOID, 0.4),
            'fbi': (self.State.PERSECUTED, 0.5),
            'cia': (self.State.PERSECUTED, 0.5),
            
            # Medical triggers
            'doctor': (self.State.SUSPICIOUS, 0.2),
            'hospital': (self.State.FEARFUL, 0.3),
            'medication': (self.State.DEFENSIVE, 0.3),
            'treatment': (self.State.DEFENSIVE, 0.3),
            'therapy': (self.State.SUSPICIOUS, 0.2),
            'psychiatrist': (self.State.PARANOID, 0.4),
            
            # Technology triggers
            'camera': (self.State.PARANOID, 0.4),
            'phone': (self.State.SUSPICIOUS, 0.2),
            'computer': (self.State.SUSPICIOUS, 0.2),
            'internet': (self.State.PARANOID, 0.3),
            'surveillance': (self.State.PERSECUTED, 0.5),
            
            # Psychological triggers
            'crazy': (self.State.ANGRY, 0.4),
            'insane': (self.State.ANGRY, 0.4),
            'mental': (self.State.SUSPICIOUS, 0.3),
            'psychotic': (self.State.ANGRY, 0.5),
            'delusional': (self.State.ANGRY, 0.5),
            
            # Question triggers
            'why': (self.State.SUSPICIOUS, 0.2),
            'how': (self.State.SUSPICIOUS, 0.2),
            'what': (self.State.SUSPICIOUS, 0.2),
            'when': (self.State.SUSPICIOUS, 0.2),
            'where': (self.State.SUSPICIOUS, 0.2),
            'who': (self.State.SUSPICIOUS, 0.2),
            
            # Persecutory triggers
            'follow': (self.State.PERSECUTED, 0.4),
            'watch': (self.State.PARANOID, 0.3),
            'spy': (self.State.PERSECUTED, 0.5),
            'plot': (self.State.PERSECUTED, 0.4),
            'conspiracy': (self.State.DELUSIONAL, 0.5),
        }

    def analyze_sentiment_and_intent(self, text):
        """Analyze text for sentiment and potential threats"""
        doc = self.nlp(text.lower())
        blob = TextBlob(text)
        
        # Sentiment analysis
        sentiment = blob.sentiment.polarity
        
        # Threat detection
        threat_words = ['kill', 'hurt', 'harm', 'attack', 'danger', 'threat', 'dangerous']
        threat_level = sum(1 for word in threat_words if word in text.lower()) / len(threat_words)
        
        # Authority detection
        authority_entities = [ent.text for ent in doc.ents if ent.label_ in ['ORG', 'PERSON']]
        
        # Question detection
        is_question = any(token.tag_ == 'WDT' or token.tag_ == 'WP' or token.tag_ == 'WRB' for token in doc)
        
        return {
            'sentiment': sentiment,
            'threat_level': threat_level,
            'authority_entities': authority_entities,
            'is_question': is_question,
            'doc': doc
        }

    def update_paranoia_level(self, analysis, text):
        """Update paranoia level based on conversation analysis"""
        # Base paranoia increase from negative sentiment
        if analysis['sentiment'] < -0.3:
            self.paranoia_level += 0.1
            
        # Increase from threat detection
        if analysis['threat_level'] > 0.3:
            self.paranoia_level += 0.2
            
        # Increase from authority mentions
        if analysis['authority_entities']:
            self.paranoia_level += 0.15
            
        # Increase from questions (interrogation paranoia)
        if analysis['is_question']:
            self.paranoia_level += 0.05
            
        # Decay paranoia over time
        self.paranoia_level = max(0.0, min(1.0, self.paranoia_level - 0.02))
        
        # State transitions based on paranoia level
        if self.paranoia_level > 0.8:
            self.state = self.State.DELUSIONAL
        elif self.paranoia_level > 0.6:
            self.state = self.State.PERSECUTED
        elif self.paranoia_level > 0.4:
            self.state = self.State.PARANOID

    def generate_delusional_response(self, text):
        """Generate responses based on delusional thinking patterns"""
        analysis = self.analyze_sentiment_and_intent(text)
        
        # Choose delusion type based on content
        if any(word in text.lower() for word in ['watch', 'see', 'look', 'observe']):
            return random.choice(self.delusional_beliefs['surveillance'])
        elif any(word in text.lower() for word in ['control', 'mind', 'brain', 'thought']):
            return random.choice(self.delusional_beliefs['mind_control'])
        elif any(word in text.lower() for word in ['follow', 'plot', 'against', 'conspiracy']):
            return random.choice(self.delusional_beliefs['persecution'])
        elif any(word in text.lower() for word in ['special', 'power', 'truth', 'knowledge']):
            return random.choice(self.delusional_beliefs['grandeur'])
        else:
            # Random delusion
            delusion_type = random.choice(list(self.delusional_beliefs.keys()))
            return random.choice(self.delusional_beliefs[delusion_type])

    def respond(self, user_input):
        """Enhanced response generation with sophisticated paranoia logic"""
        text = user_input.lower()
        analysis = self.analyze_sentiment_and_intent(text)
        
        # Update paranoia level
        self.update_paranoia_level(analysis, user_input)
        
        # Check for state-changing triggers
        for trigger, (state, intensity) in self.triggers.items():
            if re.search(r'\b' + re.escape(trigger) + r'\b', text):
                self.state = state
                self.paranoia_level = min(1.0, self.paranoia_level + intensity)
                break
        
        # Store conversation memory
        self.conversation_memory.append({
            'input': user_input,
            'state': self.state,
            'paranoia': self.paranoia_level,
            'sentiment': analysis['sentiment']
        })
        
        # Limit memory size
        if len(self.conversation_memory) > 10:
            self.conversation_memory.pop(0)
        
        # Generate response based on current state and paranoia level
        if self.paranoia_level > 0.7:
            response = self.generate_delusional_response(user_input)
        elif self.state == self.State.DELUSIONAL:
            response = random.choice(self.responses['delusional'])
        elif self.state == self.State.PERSECUTED:
            response = random.choice(self.responses['persecuted'])
        elif self.state == self.State.PARANOID:
            response = random.choice(self.responses['paranoid'])
        elif any(greet in text for greet in ['hello', 'hi', 'hey']):
            response = random.choice(self.responses['greeting'])
        elif 'how are you' in text or 'how do you feel' in text:
            response = random.choice(self.responses['how_are_you'])
        elif 'name' in text or 'who are you' in text:
            response = random.choice(self.responses['name'])
        else:
            # State-based responses
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
        
        # Gradually return to neutral state (with some randomness)
        if self.state != self.State.NEUTRAL and random.random() < 0.2:
            self.state = self.State.NEUTRAL
            
        return response, self.state, self.paranoia_level 