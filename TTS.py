import pyttsx3
import os
from sys import exit
sx3 = pyttsx3.init()
_type = input(" Drive or Computer ( g / c ) >> ")
_voice = input(" Microsoft Voice >>")
_request = input(" Insert Audio >> ")
_wav = input(" Filepath >> ")
if _type == "c":
    _user = f"C:\\Users\\{os.getlogin()}\\"
elif _type == "g":
    _user = "G:\\My Drive\\"
else:
    exit()
if _voice == "Hortense":
    sx3.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_FR-FR_HORTENSE_11.0")
elif _voice == "David":
    sx3.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
elif _voice == "Zira":
    sx3.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0")
elif _voice == "Hazel":
    sx3.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0")
elif _voice == "Heami":
   sx3.setProperty("HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_KO-KR_HEAMI_11.0")
else:
    exit() 
sx3.setProperty("rate", 150)
sx3.save_to_file(_request, f"{_user}{_wav}.wav")
sx3.runAndWait()