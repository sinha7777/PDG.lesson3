import pgzrun
import random

WIDTH=500
HEIGHT=500
TITLE="AlIENS"
messages="GAME STARTS..."

player=Actor('alien')
player.pos=100,150

def draw():
    screen.clear()
    screen.fill("brown")
    player.draw()
    screen.draw.text(messages, center=(200,20), fontsize=30, color="black")

def place_player():
    player.x=random.randint(50,450)
    player.y=random.randint(50,450)

def on_mouse_down(pos):
    print("Hi")
    global messages
    if player.collidepoint(pos):
        messages="GOOD SHOT"
        place_player()
    else:
        messages="YOU MISSED.TRY AGAIN"

place_player()
pgzrun.go()