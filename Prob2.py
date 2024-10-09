########################################
# Name: Juniper
# Collaborators: Haley
# Estimated time spent (hrs): 3
########################################

from pgl import GWindow, GRect

WIDTH = 800
HEIGHT = 600
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 15
#gw = GWindow(WIDTH,HEIGHT)
#brick= GRect(BRICK_WIDTH,BRICK_HEIGHT, x,y)

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """
    gw = GWindow(WIDTH, HEIGHT) # calls the window
    
    # Calculate the starting position
    base = HEIGHT // 2 + (BRICK_HEIGHT * BRICKS_IN_BASE) // 2 
    # setting the base for the pyramid 
    # Loop through the number of rows
    for row in range(BRICKS_IN_BASE): #putting bricks each row 
        # Calculate the number of bricks in the current row
        bricks_in_row = BRICKS_IN_BASE - row # how rows are being made 
        # Calculate the starting x position for the current row
        start_x = (WIDTH - (bricks_in_row * BRICK_WIDTH)) // 2
        # Draw the bricks in the current row
        for col in range(bricks_in_row):
            x = start_x + col * BRICK_WIDTH #simplify variable 
            y = base - row * BRICK_HEIGHT #simplify variable 
            brick = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT) # making brick arrangement 
            gw.add(brick) #adding it to g window 

if __name__ == '__main__':
    draw_pyramid()
