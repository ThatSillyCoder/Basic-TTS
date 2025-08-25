import pyttsx3
import os
sx3 = pyttsx3.init()
_user = f"C:\\Users\\{os.getlogin()}\\"
sx3.setProperty("voice", "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0")
sx3.setProperty("rate", 150)
_request = input(">> ")
_wav = input("Filepath >> ")
sx3.save_to_file(_request, f"{_user}{_wav}.wav")
sx3.runAndWait()