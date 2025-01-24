import pgzrun
import random
WIDTH=550
HEIGHT=550
stanley=Actor("blue_stánley.png")
message=""
def draw():
    screen.fill("skyblue")
    stanley.draw()
    screen.draw.text(message,center=(400,10),fontsize=30)
def update():
    pass
def on_mouse_down(pos):
    global message
    if stanley.collidepoint(pos):
        message="good shot!"
    else:
        message="try again!"





















pgzrun.go()