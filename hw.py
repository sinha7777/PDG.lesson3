import pgzrun
import random

WIDTH = 500
HEIGHT = 500
TITLE = "images"
messages = "GAME STARTS..."

# Only use the first 3 alien images
images = ["alien", "alien1", "alien2"]

player = Actor(random.choice(images))
player.pos = 100, 150

def draw():
    screen.clear()
    screen.fill("brown")
    player.draw()
    screen.draw.text(messages, center=(200, 20), fontsize=30, color="black")

def place_player():
    player.x = random.randint(50, 450)
    player.y = random.randint(50, 450)

def change_image():
    player.image = random.choice(images)

def on_mouse_down(pos):
    global messages
    print("Hi")

    if player.collidepoint(pos):
        messages = "GOOD SHOT"
        place_player()
        change_image()
    else:
        messages = "YOU MISSED. TRY AGAIN"

place_player()
pgzrun.go()
