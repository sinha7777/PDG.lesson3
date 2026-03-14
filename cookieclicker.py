import pgzrun

WIDTH=500
HEIGHT=500
TITLE="Cookie clicker game"
messages=0
player=Actor('cookie')
player.pos = 250,250

def draw():
    screen.clear()
    screen.fill("white")
    player.draw()
    screen.draw.text(str(messages),center=(250,30),fontsize=60,color="black")

def on_mouse_down(pos):
    global messages
    if player.collidepoint(pos):
        messages += 1

pgzrun.go()