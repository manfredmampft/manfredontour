from moviepy.editor import *
import numpy as np
from scipy.io.wavfile import write

# Morsecode-Tabelle
MORSE_CODE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', 
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----'
}


# Parameter
DOT = 0.2  # Sekunden
DASH = 3 * DOT
FREQUENCY = 800  # Hz
SAMPLE_RATE = 44100

def morse_to_signal(text):
    signal = []
    for char in text:
        if char == ' ':
            signal.extend([0] * int(SAMPLE_RATE * DOT * 7))  # Wortpause
        else:
            for symbol in MORSE_CODE[char.upper()]:
                duration = DOT if symbol == '.' else DASH
                t = np.linspace(0, duration, int(SAMPLE_RATE * duration), False)
                tone = np.sin(FREQUENCY * t * 2 * np.pi)
                signal.extend(tone)
                signal.extend([0] * int(SAMPLE_RATE * DOT))  # Pause zwischen Symbolen
            signal.extend([0] * int(SAMPLE_RATE * DOT * 3))  # Buchstabenpause
    return np.array(signal)

# Audio generieren
audio_signal = morse_to_signal("BOSNIEN UND HERZEGOWINA")
audio_signal = (audio_signal * 32767 / np.max(np.abs(audio_signal))).astype(np.int16)
write("morse_audio.wav", SAMPLE_RATE, audio_signal)

# Video erstellen (weiß/schwarz blinkend)
def blink_color(t):
    total_dur = 0
    pattern = []
    for c in "SOS":
        for symbol in MORSE_CODE[c]:
            dur = DOT if symbol == '.' else DASH
            pattern.append((dur, 1))  # 1=weiß
            pattern.append((DOT, 0))  # 0=schwarz
        pattern.append((DOT * 3, 0))
    total = sum(p[0] for p in pattern)
    time_in_cycle = t % total
    elapsed = 0
    for dur, color in pattern:
        if elapsed <= time_in_cycle < elapsed + dur:
            return np.array([[[color, color, color]]])
        elapsed += dur
    return np.array([[[0, 0, 0]]])

clip = VideoClip(blink_color, duration=6)
audioclip = AudioFileClip("morse_audio.wav")
video = clip.set_audio(audioclip)
video.write_videofile("morse_video.mp4", fps=10)
