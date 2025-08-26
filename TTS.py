import pyttsx3
import os
from sys import exit
sx3 = pyttsx3.init()
_type = input(" Drive or Computer ( g / c ) >> ")
_request = input(" Insert Audio >> ")
_wav = input(" Filepath >> ")
if _type == "c":
    _user = f"C:\\Users\\{os.getlogin()}\\"
elif _type == "g":
    _user = "G:\\My Drive\\"
else:
    exit()
sx3.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
sx3.setProperty("rate", 150)
sx3.save_to_file(_request, f"{_user}{_wav}.wav")
sx3.runAndWait()