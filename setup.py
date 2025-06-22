#!/usr/bin/env python3
"""
Setup script for Advanced Parry Chatbot
Installs required NLP models and creates placeholder sound files
"""

import os
import subprocess
import sys

def run_command(command, description):
    """Run a shell command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_directories():
    """Create necessary directories"""
    directories = [
        'static/sounds',
        'static/backgrounds',
        'templates'
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)
        print(f"📁 Created directory: {directory}")

def create_placeholder_sounds():
    """Create placeholder sound files"""
    sound_files = {
        'neutral': ['neutral1.mp3', 'neutral2.mp3'],
        'suspicious': ['suspicious1.mp3', 'suspicious2.mp3'],
        'angry': ['angry1.mp3', 'angry2.mp3'],
        'fearful': ['fearful1.mp3', 'fearful2.mp3'],
        'defensive': ['defensive1.mp3', 'defensive2.mp3'],
        'paranoid': ['paranoid1.mp3', 'paranoid2.mp3'],
        'delusional': ['delusional1.mp3', 'delusional2.mp3'],
        'persecuted': ['persecuted1.mp3', 'persecuted2.mp3'],
        'background': ['ambient_creepy.mp3']
    }
    
    for category, files in sound_files.items():
        for filename in files:
            filepath = os.path.join('static/sounds', filename)
            if not os.path.exists(filepath):
                # Create a simple text file as placeholder
                with open(filepath, 'w') as f:
                    f.write(f"# Placeholder for {filename}\n")
                    f.write(f"# Replace with actual audio file for {category} state\n")
                print(f"📄 Created placeholder: {filepath}")

def install_requirements():
    """Install Python requirements"""
    print("📦 Installing Python requirements...")
    return run_command("pip install -r requirements.txt", "Installing Python packages")

def install_spacy_model():
    """Install spaCy English model"""
    print("🧠 Installing spaCy English model...")
    return run_command("python -m spacy download en_core_web_sm", "Installing spaCy model")

def main():
    print("🚀 Setting up Advanced Parry Chatbot...")
    print("=" * 50)
    
    # Create directories
    create_directories()
    
    # Install requirements
    if not install_requirements():
        print("❌ Failed to install requirements. Please check your Python environment.")
        sys.exit(1)
    
    # Install spaCy model
    if not install_spacy_model():
        print("❌ Failed to install spaCy model. Please try manually:")
        print("   python -m spacy download en_core_web_sm")
        sys.exit(1)
    
    # Create placeholder sounds
    create_placeholder_sounds()
    
    print("\n" + "=" * 50)
    print("✅ Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Replace placeholder sound files in static/sounds/ with actual audio files")
    print("2. Run the basic version: python app.py")
    print("3. Run the advanced version: python app_advanced.py")
    print("\n🎵 Sound file recommendations:")
    print("- Use short, atmospheric sounds for different emotional states")
    print("- Background music should be ambient and creepy")
    print("- Keep file sizes small for web compatibility")
    print("\n🌐 Open http://localhost:5000 in your browser to chat with Parry!")

if __name__ == "__main__":
    main() 