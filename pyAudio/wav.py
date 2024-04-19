import pyaudio
import wave
import time
import numpy as np
import requests

P = 1
S = 0

class Music():
    def __init__(self, note_map):
        self.note_map = note_map
        self.sample_rate = 126200 # frequência, era 44100, com muitos ruídos
        self.channels = 1
        self.p = pyaudio.PyAudio()
        self.numbers = [str(i) for i in range(10)]
        self.u_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
        self.m_letters = [chr(i) for i in range(ord('a'), ord('z')+ 1)]
        self.original_array = self.numbers + self.m_letters + self.u_letters
    
    def play_sound(self, frequency, duration):
        t = np.linspace(0, duration, int(self.sample_rate * duration), False)
        audio_data = np.sin(2 * np.pi * frequency * t)

        stream = self.p.open(format=pyaudio.paFloat32, channels=self.channels, rate=self.sample_rate, output=True)
        stream.write(audio_data.tobytes())

        stream.stop_stream()
        stream.close()
    
    def play_music(self, note_array):
        duration = 0.1
        self.original_array 
        print(note_array)
        verify = set(note_array).issubset(set(self.original_array))
        if verify:
            for note in note_array:
                if note in self.note_map:
                    frequency = self.note_map[note]
                    if note.isdigit():
                        duration = note
                    self.play_sound(frequency, duration) 
                    # time.sleep(0.005)  # pausa default
                else:
                    print(f"Note '{note}' not found in the map.")
        else:
            print("Something Went Wrong :(")
                
notesMap = {
"C" : 261.63, # dó
"H" : 277.18 ,# dó#
"D" : 293.66, # ré
"I" : 311.13, # ré$
"E" : 329.63, #mi 
"F" : 349.23, #fá
"J" : 369.99, #fá#
"G" : 392.00 , #sol
"K" : 415.30, #sol#
"A" : 440.00, #la
"L" : 466.16 , #la#
"B" : 493.88, #si
"Q" : 523.26,
"M" : 659.26 #mi5
}

durationMap = {
    1 : 0.2, # 1 em 100 bpm
    2 : 0.4, #acho que cabe 1 e meia em 100bpm kk
    3 : 0.6, #cabe 2 em 100 bpm
    4 : 0.8, #cabe 3 em 100 bpm
    5 : 1.0  #cabe 4 em 100 bpm    
}

class MusicPlayer(Music):
    def __init__(self, note_map):
        super().__init__(note_map)

    def get_request(self, url):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return response.text
            else:
                print(f"Error: {response.status_code}")
                return None
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def play_music_from_api(self, url):
        data = self.get_request(url)
        if data:
            note_array = list(data) # Assuming data is a comma-separated list of notes
            self.play_music(note_array)
        else:
            print("Failed to retrieve data from the API.")

# Exemplo de uso:
url = "http://127.0.0.1:5000/predict/"
player = MusicPlayer(notesMap)
player.play_music_from_api(url)
