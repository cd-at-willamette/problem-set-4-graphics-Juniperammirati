########################################
# Name: Juniper 
# Collaborators:
# Estimate time spent (hrs):1
########################################
# accidentally deleted the clicky_box function at the start and don't know how to add it back after I made my code
from pgl import GWindow, GRect, GLabel, GLine
import random

GW_WIDTH = 500                      # Width of window
GW_HEIGHT = 500                     # Height of window
SQUARE_SIZE = 50                    # Width and height of square
SCORE_DX = 10                       # Distance from left of window to origin
SCORE_DY = 10                       # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"    # Font for score
SQUARE_COLOR = "red"               # Square color

# Create the graphics window
gw = GWindow(GW_WIDTH, GW_HEIGHT)

# creating starting square
starting_x = (GW_WIDTH - SQUARE_SIZE) // 2 # middle for x axis
starting_y = (GW_HEIGHT - SQUARE_SIZE) // 2 # middle for y axis
gw.box = GRect(starting_x, starting_y, SQUARE_SIZE, SQUARE_SIZE) # putting into position 
gw.box.set_filled(True) # coloring in the box 
gw.box.set_color(SQUARE_COLOR) # setting the box to a color 
gw.add(gw.box) # adding original box 

# Starting score 
click_count = 0 # click count determine what changes in score 
score_label = GLabel(f"Score: {click_count}")
score_label.set_font(SCORE_FONT) # making correct font 
score_label.set_location(SCORE_DX, GW_HEIGHT - SCORE_DY) #setting the score into position on the gwindow
gw.add(score_label)# displying it to the gw

# knowing player is clicking (like enter action function)
def click_func(e):
    global click_count
    x = e.get_x()
    y = e.get_y()
    
    # Check if the click is inside the box
    if (gw.box.get_x() <= x <= gw.box.get_x() + gw.box.get_width() and
        gw.box.get_y() <= y <= gw.box.get_y() + gw.box.get_height()):
        click_count += 1 # changing the click count to help change the score and move the box 
        move_box_randomly() # moving the box 
    else:
        click_count = 0  # Reset score if clicked outside
    
    update_score_display()

# move the box to a random position
def move_box_randomly():
    # Generate random coordinates within the window 
    new_x = random.randint(0, GW_WIDTH - SQUARE_SIZE)
    new_y = random.randint(0, GW_HEIGHT - SQUARE_SIZE)
    gw.box.set_location(new_x, new_y) # putting into location

def update_score_display():
    score_label.set_label(f"Score: {click_count}") 

# Add the click event listener
gw.add_event_listener("click", click_func)









if __name__ == '__main__':
    clicky_box()
