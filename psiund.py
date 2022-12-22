from playsound import playsound
import threading

def pl(url:str):
  playsound(url)



threading.Thread(target=playsound, args=(
    'https://www.myinstants.com/media/sounds/who-tf-is-giga-n-gga.mp3',), daemon=False).start()

# pl('https://www.myinstants.com/media/sounds/who-tf-is-giga-n-gga.mp3')


