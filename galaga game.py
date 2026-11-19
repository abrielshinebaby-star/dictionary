import pgzrun,random

WIDTH=600
HEIGHT=600
TITLE="GALAGA GAME"

space_ship=Actor("space_ship")
space_ship.x=300
space_ship.y=550

bee=Actor("bee")
bee.x=300
bee.y=50

score=0

def draw():
    screen.fill("black")
    space_ship.draw()
    bee.draw()
    screen.draw.text("score"+str(score),(50,50))
    for bullet in bullets:
        bullet.draw()
    
def on_key_down(key):
    if key==keys.SPACE:
        bullet=Actor("bullet")
        bullet.x=space_ship.x
        bullet.y=space_ship.y
        bullets.append(bullet)


bullets=[]
def update():
    global score
    if keyboard.a:
        space_ship.x=space_ship.x-5
    if keyboard.d:
        space_ship.x=space_ship.x+5
    for bullet in bullets:
        bullet.y=bullet.y-3
        if bullet.colliderect(bee):
            bee.x=random.randint(0,600)
            bee.y=0
            score+=1
            bullets.remove(bullet)
    bee.y=bee.y+3
    if bee.y>=600:
        bee.pos=(random.randint(0,550),0)





pgzrun.go()