import pyttsx3


def text_to_speech(text):
    """
    Convert text to speech.

    Parameters
    ----------
    text : str
        The text to be converted to speech.

    """
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
