class ParryChat {
    constructor() {
        this.chatWindow = document.getElementById('chat-window');
        this.chatForm = document.getElementById('chat-form');
        this.userInput = document.getElementById('user-input');
        this.paranoiaFill = document.getElementById('paranoia-fill');
        this.paranoiaText = document.getElementById('paranoia-text');
        this.backgroundMusic = document.getElementById('background-music');
        this.soundEffect = document.getElementById('sound-effect');
        this.toggleSoundBtn = document.getElementById('toggle-sound');
        this.toggleBgBtn = document.getElementById('toggle-bg');
        
        this.soundEnabled = true;
        this.bgMusicEnabled = true;
        this.isTyping = false;
        
        this.init();
    }
    
    init() {
        this.setupEventListeners();
        this.startBackgroundMusic();
        this.updateParanoiaMeter(0, 'Neutral');
    }
    
    setupEventListeners() {
        this.chatForm.addEventListener('submit', (e) => this.handleSubmit(e));
        this.toggleSoundBtn.addEventListener('click', () => this.toggleSound());
        this.toggleBgBtn.addEventListener('click', () => this.toggleBackgroundMusic());
        
        // Add typing effect
        this.userInput.addEventListener('input', () => {
            if (!this.isTyping) {
                this.isTyping = true;
                this.playTypingSound();
            }
        });
        
        this.userInput.addEventListener('keyup', () => {
            setTimeout(() => {
                this.isTyping = false;
            }, 1000);
        });
    }
    
    async handleSubmit(e) {
        e.preventDefault();
        const message = this.userInput.value.trim();
        if (!message) return;
        
        // Add user message
        this.addMessage('user', message);
        this.userInput.value = '';
        
        // Show typing indicator
        this.showTypingIndicator();
        
        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message })
            });
            
            const data = await response.json();
            
            // Remove typing indicator
            this.removeTypingIndicator();
            
            // Add Parry's response
            this.addMessage('parry', `Parry: ${data.response}`, data.state);
            
            // Update paranoia meter
            this.updateParanoiaMeter(data.paranoia_level, data.state);
            
            // Play sound effect
            if (this.soundEnabled && data.sound_effect) {
                this.playSoundEffect(data.sound_effect);
            }
            
            // Scroll to bottom
            this.scrollToBottom();
            
        } catch (error) {
            console.error('Error:', error);
            this.removeTypingIndicator();
            this.addMessage('parry', 'Parry: I... I can\'t hear you properly. The voices are too loud.');
        }
    }
    
    addMessage(sender, text, state = null) {
        const div = document.createElement('div');
        div.className = `message ${sender}`;
        
        const messageText = document.createElement('span');
        messageText.className = 'message-text';
        messageText.textContent = text;
        
        const messageTime = document.createElement('span');
        messageTime.className = 'message-time';
        messageTime.textContent = state ? `[State: ${state}]` : `[${new Date().toLocaleTimeString()}]`;
        
        div.appendChild(messageText);
        div.appendChild(messageTime);
        
        this.chatWindow.appendChild(div);
        
        // Add special effects for Parry's messages
        if (sender === 'parry') {
            this.addParryEffects(div, state);
        }
    }
    
    addParryEffects(messageElement, state) {
        // Add glitch effect for delusional state
        if (state === 'delusional') {
            messageElement.style.animation = 'glitch 0.3s ease-in-out';
            setTimeout(() => {
                messageElement.style.animation = '';
            }, 300);
        }
        
        // Add shake effect for angry state
        if (state === 'angry') {
            messageElement.style.animation = 'shake 0.5s ease-in-out';
            setTimeout(() => {
                messageElement.style.animation = '';
            }, 500);
        }
        
        // Add pulse effect for paranoid state
        if (state === 'paranoid') {
            messageElement.style.animation = 'pulse 2s ease-in-out infinite';
        }
    }
    
    showTypingIndicator() {
        const typingDiv = document.createElement('div');
        typingDiv.className = 'message parry typing-indicator';
        typingDiv.id = 'typing-indicator';
        
        const dots = document.createElement('span');
        dots.className = 'typing-dots';
        dots.textContent = 'Parry is typing';
        
        typingDiv.appendChild(dots);
        this.chatWindow.appendChild(typingDiv);
        this.scrollToBottom();
    }
    
    removeTypingIndicator() {
        const typingIndicator = document.getElementById('typing-indicator');
        if (typingIndicator) {
            typingIndicator.remove();
        }
    }
    
    updateParanoiaMeter(level, state) {
        const percentage = level * 100;
        this.paranoiaFill.style.width = `${percentage}%`;
        this.paranoiaText.textContent = state;
        
        // Change meter color based on level
        if (level > 0.7) {
            this.paranoiaFill.style.background = 'linear-gradient(90deg, #ff0000, #ff4444)';
        } else if (level > 0.4) {
            this.paranoiaFill.style.background = 'linear-gradient(90deg, #ffff00, #ffaa00)';
        } else {
            this.paranoiaFill.style.background = 'linear-gradient(90deg, #00ff00, #44ff44)';
        }
    }
    
    playSoundEffect(soundFile) {
        if (!this.soundEnabled) return;
        
        this.soundEffect.src = `/static/sounds/${soundFile}`;
        this.soundEffect.volume = 0.3;
        this.soundEffect.play().catch(e => console.log('Sound effect failed to play:', e));
    }
    
    playTypingSound() {
        if (!this.soundEnabled) return;
        
        // Create a simple typing sound
        const audioContext = new (window.AudioContext || window.webkitAudioContext)();
        const oscillator = audioContext.createOscillator();
        const gainNode = audioContext.createGain();
        
        oscillator.connect(gainNode);
        gainNode.connect(audioContext.destination);
        
        oscillator.frequency.setValueAtTime(800, audioContext.currentTime);
        oscillator.frequency.exponentialRampToValueAtTime(600, audioContext.currentTime + 0.1);
        
        gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.1);
        
        oscillator.start(audioContext.currentTime);
        oscillator.stop(audioContext.currentTime + 0.1);
    }
    
    startBackgroundMusic() {
        if (this.bgMusicEnabled) {
            this.backgroundMusic.volume = 0.2;
            this.backgroundMusic.play().catch(e => console.log('Background music failed to play:', e));
        }
    }
    
    toggleSound() {
        this.soundEnabled = !this.soundEnabled;
        this.toggleSoundBtn.textContent = `🔊 Sound: ${this.soundEnabled ? 'ON' : 'OFF'}`;
        
        if (!this.soundEnabled) {
            this.soundEffect.pause();
            this.soundEffect.currentTime = 0;
        }
    }
    
    toggleBackgroundMusic() {
        this.bgMusicEnabled = !this.bgMusicEnabled;
        this.toggleBgBtn.textContent = `🎵 Background: ${this.bgMusicEnabled ? 'ON' : 'OFF'}`;
        
        if (this.bgMusicEnabled) {
            this.backgroundMusic.play().catch(e => console.log('Background music failed to play:', e));
        } else {
            this.backgroundMusic.pause();
        }
    }
    
    scrollToBottom() {
        this.chatWindow.scrollTop = this.chatWindow.scrollHeight;
    }
}

// Add CSS animations
const style = document.createElement('style');
style.textContent = `
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(-2px, -2px); }
        60% { transform: translate(2px, 2px); }
        80% { transform: translate(2px, -2px); }
        100% { transform: translate(0); }
    }
    
    @keyframes shake {
        0%, 100% { transform: translateX(0); }
        10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
        20%, 40%, 60%, 80% { transform: translateX(5px); }
    }
    
    @keyframes pulse {
        0%, 100% { opacity: 1; }
        50% { opacity: 0.7; }
    }
    
    .typing-indicator {
        opacity: 0.7;
        font-style: italic;
    }
    
    .typing-dots::after {
        content: '';
        animation: dots 1.5s steps(5, end) infinite;
    }
    
    @keyframes dots {
        0%, 20% { content: ''; }
        40% { content: '.'; }
        60% { content: '..'; }
        80%, 100% { content: '...'; }
    }
`;
document.head.appendChild(style);

// Initialize the chat when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new ParryChat();
}); 