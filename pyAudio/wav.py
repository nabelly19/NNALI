import pyaudio
import wave
import notes
import time
import numpy as np

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
        duration = 0.2
        self.original_array 
        verify = set(note_array).issubset(set(self.original_array))
        if verify:
            for note in note_array:
                if note in self.note_map:
                    frequency = self.note_map[note]
                    if note.isdigit():
                        duration = note
                    self.play_sound(frequency, duration) 
                    time.sleep(0.1)  # pausa default
                else:
                    print(f"Note '{note}' not found in the map.")
        else:
            print("Something Went Wrong :(")
                
notesMap = {
"C" : 261.63,
"H" : 277.18 ,
"D" : 293.66,
"I" : 311.13,
"E" : 329.63,
"F" : 349.23,
"J" : 369.99,
"G" : 392.00 ,
"K" : 415.30,
"A" : 440.00,
"L" : 466.16 ,
"B" : 493.88,
}

durationMap = {
    1 : 0.2, # 1 em 100 bpm
    2 : 0.4, #acho que cabe 1 e meia em 100bpm kk
    3 : 0.6, #cabe 2 em 100 bpm
    4 : 0.8, #cabe 3 em 100 bpm
    5 : 1.0  #cabe 4 em 100 bpm    
}


    
my_notes = ["E", "G", "G", "G", "A", "A", "A"]  # Replace with your array of notes
player = Music(notesMap)
player.play_music(my_notes)


# cemitério :(

 # def play_music(self, str_view:str):
    #     self.original_array 
    #     verify = set(str_view).issubset(set(self.original_array))
        
    #     if verify:
    #         for i in range(str_view):
    #             try: 
    #                 self._notes[str_view][P] = self._notes[str_view][S].play()
    #             except:
    #                 return "Erro ao ler música"

                
                    
            
            


