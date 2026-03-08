import psutil
import time
import os
import subprocess
from gtts import gTTS
import pygame

pygame.mixer.init()

def warning_suara(teks):
    tts = gTTS(text=teks, lang='id')
    tts.save("warning.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("warning.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        time.sleep(0.1)
    pass

def get_temp():
    temps = psutil.sensors_temperatures()
    if 'coretemp' in temps:
        return temps['coretemp'][0].current
    return None
    
last_temp = get_temp()
last_time = time.time()

def calculate(current_temp):
    global last_temp, last_time
    
    now = time.time()
    dt = now - last_time
    dT = current_temp - last_temp
    
    laju = dT / dt if dt > 0 else 0
    
    last_temp = current_temp
    last_time = now
    
    return laju

def action():
    subprocess.run(["mode-dingin"]) 
    print("Switched to cool mode")

try:
    while True:
        current_temp = get_temp()
        laju = calculate(current_temp)
        
        print(f"Temp: {current_temp}°C | Laju: {laju:.2f}°C/s")
        
        if current_temp > 75:
            action()
            warning_suara("Suhu kritis! Laptop lu panas banget bro, istirahat dulu!")

        elif laju > 1.5: 
            warning_suara("Woi, suhu naik kencang banget! Ada proses berat ya?")
            
        time.sleep(2)
        
except KeyboardInterrupt:
    print("Sentinel berhenti bertugas.")

print(f"Suhu CPU saat ini: {get_temp()}°C")