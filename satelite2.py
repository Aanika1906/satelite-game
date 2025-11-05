import pgzrun
import random

TITLE="~~~*CONNECT THE CIRCUIT :)*~~~"
WIDTH=500  
HEIGHT=500
numberofsatelites=8
nextsatelite=0
lines=[]
satelites=[]
gameover=False

def createsatelites():
    for i in range(0,numberofsatelites):#to creat multiple satelites
        satelite=Actor("satelitepicture.png")
        satelite.pos= random.randint(20,450),random.randint(20,450)#position of satelited randomised
        satelites.append(satelite)

def draw():
    screen.clear()
    screen.blit("galaxybackground.png",(0,0))
    number=1
    for i in satelites:
      i.draw()
      screen.draw.text(str(number),(i.pos[0],i.pos[1]+20),color="red")#writes the numbers where the sats are (+20 the number is below the image)
      number=number+1
    for line in lines:
        screen.draw.line(line[0],line[1],color="red")#draws the line
    if nextsatelite==numberofsatelites:
        screen.fill("black")
        screen.draw.text("GAME OVER",(250,250),color="white",fontsize=30)

def update() :
    pass#updates the screen

def on_mouse_down(pos):#captures the position where the mouse is pressed
    global nextsatelite,lines
    if nextsatelite<numberofsatelites:#first point is the nnumber of the satelite should be less than the total sats
        if satelites[nextsatelite].collidepoint(pos):#so the collide point should be of the next satelite which is hweere ur mesnt to press the mouse
            if nextsatelite:#if nextsatelite contains "True"
                lines.append((satelites[nextsatelite-1].pos,satelites[nextsatelite].pos))#appending the previous satelite position and the previous satelite position in the lines list
            nextsatelite=nextsatelite+1#so u move on the satelite like  the starting position of the next sat will be different
            
        
        
        else:
            lines=[]#everything will be gone so  the lines will be empty
            nextsatelite=0#so it reuurns back to 0 if you get the next satelite wrong


createsatelites()    





pgzrun.go()