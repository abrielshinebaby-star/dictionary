import pgzrun
WIDTH=400
HEIGHT=400
TITLE="Shapes"

rect1=Rect((300,300),(50,100))

def draw():
    screen.fill("cyan")
    screen.draw.circle((200,200),90,"turquoise")
    screen.draw.filled_circle((100,200),90,"turquoise")
    screen.draw.filled_rect(rect1,"red")
    screen.draw.line((100,100),(100,300),"black")
def update():
    pass

pgzrun.go()