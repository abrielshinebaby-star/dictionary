import pgzrun

HEIGHT=600
WIDTH=600
TITLE="bumble bee and the flower"

bee=Actor("bumble bee")
bee.x=300
bee.y=550

flower=Actor("flower")
flower.x=300
flower.y=300

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()



def update():
    if keyboard.left:
        bee.x=bee.x-1

pgzrun.go()