import pyaudio
import wave
import notes
import simpleaudio

P = 1
S = 0

class Music():
    def __init__(self) -> None:
        pass
    
    numbers = [str(i) for i in range(10)]
    u_letters = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
    m_letters = [chr(i) for i in range(ord('a'), ord('z')+ 1)]
    
    original_array = numbers + m_letters + u_letters
    
    def playMusic(self, str_view):
        self.original_array 
        verify = set(str_view).issubset(set(self.original_array))
        
        if verify:
            for i in range(str_view):
                try:    
                    
            
            


