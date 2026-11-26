import pgzrun,random

WIDTH= 600
HEIGHT= 600
TITLE= "connect the satelites"

satelites=[]

for i in range(7):
    satelite=Actor("satelite")
    satelite.x=random.randint(0,600)
    satelite.y=random.randint(0,600)

    satelites.append(satelite)

def draw():
    screen.blit("space",(0,0))
    number=1
    for satelite in satelites:
        satelite.draw()
        screen.draw.text(str(number),(satelite.x,satelite.y+25))
        number+=1


def update():
    pass


pgzrun.go()