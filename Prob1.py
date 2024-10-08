############################################################
# Name: Juniper 
# Name(s) of anyone worked with:
# Est time spent (hr): 1
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window

    gw = GWindow(WIDTH, HEIGHT)
    
    rect = GRect(0,0,600,600) 
    rect.set_color("Black")
    rect.set_filled(True) 
    gw.add(rect)

    line = GLine(0,10,600,10) 
    line.set_color("Red") 
    gw.add(line)

    line = GLine(0,50,600,50) 
    line.set_color("Blue") 
    gw.add(line)

    line = GLine(0,100,600,100) 
    line.set_color("Yellow") 
    gw.add(line)

    line = GLine(0,150,600,150) 
    line.set_color("Green") 
    gw.add(line)

    rect = GRect(45,25,510,400) 
    rect.set_color("White")
    rect.set_filled(True) 
    gw.add(rect)

    Oval=GOval(50,100, 200,200)
    Oval.set_color("Blue")
    gw.add(Oval)

    Oval=GOval(150,200 ,200,200)
    Oval.set_color("Yellow")
    gw.add(Oval)

    Oval=GOval(300,200, 200,200)
    Oval.set_color("Green")
    gw.add(Oval)

    Oval=GOval(350,100, 200,200)
    Oval.set_color("Red")
    gw.add(Oval)

    Oval=GOval(200,100, 200,200)
    Oval.set_color("Black")
    gw.add(Oval)
    
    gw.add(GLabel("Olympics!", 300, 50)) 
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    
    
    

    

   


    

if __name__ == '__main__':
    draw_image()


