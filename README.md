A cutting-edge recreation of the original Parry chatbot with advanced NLP, psychological modeling, and immersive spooky interface.

🌟 Features

🤖 Advanced AI Engine

Sophisticated NLP: Uses spaCy and TextBlob for natural language understanding
Psychological Modeling: Implements real paranoid schizophrenia patterns
State Machine: 8 different emotional states with complex transitions
Memory System: Remembers conversation context and builds paranoia over time
Delusional Thinking: Generates responses based on specific delusion types
🎨 Immersive Interface

Spooky Visuals: Animated backgrounds, fog effects, and glowing elements
Real-time Paranoia Meter: Visual indicator of Parry's mental state
Sound Effects: Atmospheric audio for different emotional states
Background Music: Creepy ambient soundtrack
Visual Effects: Glitch, shake, and pulse animations based on state
🧠 Psychological States

Neutral: Baseline conversational state
Suspicious: Triggered by questions and medical terms
Angry: Triggered by psychological labels
Fearful: Triggered by authority figures
Defensive: Triggered by treatment-related topics
Paranoid: Advanced suspicion and mistrust
Delusional: Full delusional thinking patterns
Persecuted: Feeling of being targeted
🚀 Quick Start

Prerequisites

Python 3.7+
pip package manager
Installation

Clone or download the project files

Run the setup script:

python setup.py
This will:

Install all required Python packages
Download spaCy English language model
Create necessary directories
Generate placeholder sound files
Start the advanced version:

python app_advanced.py
Open your browser to http://localhost:5000

🎵 Sound Setup

The system expects sound files in static/sounds/:

Required Sound Files

ambient_creepy.mp3 - Background music
neutral1.mp3, neutral2.mp3 - Neutral state sounds
suspicious1.mp3, suspicious2.mp3 - Suspicious state sounds
angry1.mp3, angry2.mp3 - Angry state sounds
fearful1.mp3, fearful2.mp3 - Fearful state sounds
defensive1.mp3, defensive2.mp3 - Defensive state sounds
paranoid1.mp3, paranoid2.mp3 - Paranoid state sounds
delusional1.mp3, delusional2.mp3 - Delusional state sounds
persecuted1.mp3, persecuted2.mp3 - Persecuted state sounds
Sound Recommendations

Background Music: Ambient, atmospheric, 5-10 minutes loop
State Sounds: Short (2-5 seconds), atmospheric effects
Format: MP3 for web compatibility
Volume: Keep levels moderate for web playback
🧠 How It Works

NLP Analysis

The system analyzes user input using:

Sentiment Analysis: Detects emotional tone
Entity Recognition: Identifies people, organizations, locations
Question Detection: Recognizes interrogative patterns
Threat Assessment: Evaluates potential dangers
Paranoia Modeling

Parry's paranoia level (0.0-1.0) increases based on:

Negative sentiment in user messages
Mentions of authority figures
Questions (interpreted as interrogation)
Threat-related vocabulary
Medical or psychological terms
State Transitions

States change based on:

Trigger Words: Specific terms that immediately change state
Paranoia Level: Gradual progression through states
Conversation Context: Memory of previous interactions
Random Recovery: Occasional return to neutral state
Delusional Responses

When paranoia is high (>0.7), Parry generates responses based on:

Surveillance Delusions: "They're watching me"
Mind Control Delusions: "They're controlling my thoughts"
Persecution Delusions: "Everyone is plotting against me"
Grandeur Delusions: "I have special powers"
🎮 Usage Tips

Triggering Different States

Suspicious: Ask questions ("Why?", "How?", "What?")
Angry: Use psychological terms ("crazy", "insane", "mental")
Fearful: Mention authority ("police", "government", "FBI")
Defensive: Discuss treatment ("medication", "therapy", "hospital")
Paranoid: Talk about surveillance ("cameras", "watching", "spying")
Delusional: Mention conspiracy or control ("conspiracy", "mind control")
Interface Controls

Sound Toggle: Enable/disable sound effects
Background Toggle: Enable/disable ambient music
Paranoia Meter: Real-time visualization of mental state
State Indicators: Shows current emotional state
🔧 Technical Details

Architecture

Backend: Flask web server with REST API
Frontend: HTML5/CSS3/JavaScript with Web Audio API
NLP: spaCy + TextBlob for language processing
State Management: Python class with memory and history
Key Components

parry_advanced.py: Core AI logic with NLP and psychology
app_advanced.py: Flask web server
templates/index_advanced.html: Enhanced UI template
static/style_advanced.css: Spooky visual styling
static/chat_advanced.js: Interactive frontend logic
Dependencies

Flask: Web framework
spaCy: Natural language processing
TextBlob: Sentiment analysis
NLTK: Text processing utilities
🎭 Historical Context

This advanced version builds upon the original Parry (1972) by Kenneth Colby, incorporating:

Modern NLP techniques
Psychological research on paranoid schizophrenia
Contemporary web technologies
Immersive user experience design
The original Parry was groundbreaking for demonstrating that computers could simulate human psychological states. This version extends that concept with sophisticated language understanding and realistic paranoia modeling.

🚨 Disclaimer

This is an educational recreation for learning purposes. The psychological patterns are based on research but are simplified for demonstration. This is not a medical tool and should not be used for clinical purposes.

🤝 Contributing

Feel free to enhance the system by:

Adding more sophisticated NLP patterns
Improving the psychological modeling
Creating better sound effects
Enhancing the visual interface
Adding more delusional thinking patterns
📄 License

Educational use only. This recreation is for learning and research purposes.
