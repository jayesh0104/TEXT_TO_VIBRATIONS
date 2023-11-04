import pygame
import time
from flask import Flask, render_template, request

app = Flask(__name__)

pygame.init()

vibration_patterns = {
    'A': ['.','-',' ',' ',' '],
    'B': ['-','.','.','.',' '],
    'C': ['-','.','-','.',' '],
    'D': ['-','.','.',' ',' '],
    'E': ['.',' ',' ',' ',' '],
    'F': ['.','.','-','.',' '],
    'G': ['-','-','.',' ',' '],
    'H': ['.','.','.','.',' '],
    'I': ['.','.',' ',' ',' '],
    'J': ['.','-','-','-',' '],
    'K': ['-','.','-',' ',' '],
    'L': ['.','-','.','.',' '],
    'M': ['-','-',' ',' ',' '],
    'N': ['-','.',' ',' ',' '],
    'O': ['-','-','-',' ',' '],
    'P': ['.','-','-','.',' '],
    'Q': ['-','-','.','-',' '],
    'R': ['.','-','.',' ',' '],
    'S': ['.','.','.',' ',' '],
    'T': ['-',' ',' ',' ',' '],
    'U': ['.','.','-',' ',' '],
    'V': ['.','.','.','-',' '],
    'W': ['.','-','-',' ',' '],
    'X': ['-','.','.','-',' '],
    'Y': ['-','.','-','-',' '],
    'Z': ['-','-','.','.',' '],
    ' ': ['.','.','.','.',' '],
    '1': ['.','-','-','-','-'],
    '2': ['.','.','-','-','-'],
    '3': ['.','.','.','-','-'],
    '4': ['.','.','.','.','-'],
    '5': ['.','.','.','.','.'],
    '6': ['-','.','.','.','.'],
    '7': ['-','-','.','.','.'],
    '8': ['-','-','-','.','.'],
    '9': ['-','-','-','-','.'],
    '0': ['-','-','-','-','-']
}

def text_to_vibrations(text):
    vibrations = []
    for char in text:
        char = char.upper()  # Convert to uppercase for simplicity
        if char in vibration_patterns:
            vibrations.extend(vibration_patterns[char])
        else:
            vibrations.extend(vibration_patterns[' '])
    return vibrations


def create_vibrations(pattern):
    pygame.mixer.init()
    for v in pattern:
        if v == '-':
            pygame.mixer.music.load("vibration.wav")  # Replace with an actual vibration sound
            pygame.mixer.music.play()
        elif v == '.':
            pygame.mixer.music.load("vibration_2.wav")  # Replace with an actual vibration sound
            pygame.mixer.music.play()
        time.sleep(1)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST']) 
def convert(): 
    message = request.form['text'] 
    vibration_pattern = text_to_vibrations(message)
    create_vibrations(vibration_pattern)
    return 'Vibrations played'

if __name__ == '__main__':
    app.run(debug=True)
