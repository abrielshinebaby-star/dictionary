import pgzrun,random

HEIGHT=600
WIDTH=600
TITLE="bumble bee and the flower"

bee=Actor("bumble bee")
bee.x=300
bee.y=550

flower=Actor("flower")
flower.x=300
flower.y=300

score=0

def draw():
    screen.blit("background",(0,0))
    bee.draw()
    flower.draw()
    screen.draw.text("score"+str(score),(200,200))



def update():
    global score
    if keyboard.a:
        bee.x=bee.x-5
    if keyboard.d:
        bee.x=bee.x+5
    if keyboard.w:
        bee.y=bee.y-5
    if keyboard.s:
        bee.y=bee.y+5
    if bee.colliderect(flower):
        flower.x=random.randint(50,550)
        flower.y=random.randint(50,550)
        score+=1
        
    
    

pgzrun.go()