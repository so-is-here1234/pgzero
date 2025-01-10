import pgzrun
import random
WIDTH=350
HEIGHT=350
def draw():
    length=350
    height=200

    for i in range(20):
        red=random.randint(0,255)
        green=random.randint(0,255)
        blue=random.randint(0,255)
        rect=Rect((0,0),(length,height))
        rect.center=175,175
        screen.draw.rect(rect,(red,green,blue))
        length-=10
        height+=10
def update():
    pass


























pgzrun.go()