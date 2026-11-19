import pgzrun,random

WIDTH= 600
HEIGHT= 600
TITLE= "connect the satelites"

satelite=Actor("satelite")
satelite.x=random.randint(0,300)
satelite.y=random.randint(0,300)

def draw():
    screen.blit("space",(0,0))
    satelite.draw()


pgzrun.go()