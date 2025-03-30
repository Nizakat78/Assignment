from graphics import GraphWin, Rectangle, Point
import time

CANVAS_WIDTH : int = 400
CANVAS_HEIGHT : int = 400

CELL_SIZE : int = 40
ERASER_SIZE : int =40

def erase_objects(win, eraser):
    """Erase objects in contact with the eraser"""
    mouse_x = win.getMouse().getX()
    mouse_y = win.getMouse().getY()
    
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Use GraphWin's method to find overlapping objects (if such method exists in this library)
    overlapping_objects = win.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            overlapping_object.setFill('white')  # Change color of overlapping objects to white

def main():
    win = GraphWin("Erase Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    
    num_rows = CANVAS_HEIGHT // CELL_SIZE  # Calculate number of rows
    num_cols = CANVAS_WIDTH // CELL_SIZE   # Calculate number of columns
    
    # Draw the grid of squares
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            cell = Rectangle(Point(left_x, top_y), Point(right_x, bottom_y))
            cell.setFill('blue')
            cell.draw(win)
    
    win.getMouse()  # Wait for the user to click to start creating the eraser
    
    last_click_x, last_click_y = win.getMouse().getX(), win.getMouse().getY()
    
    # Create the eraser (pink square)
    eraser = Rectangle(Point(last_click_x, last_click_y), 
                       Point(last_click_x + ERASER_SIZE, last_click_y + ERASER_SIZE))
    eraser.setFill('pink')
    eraser.draw(win)
    
    # Move the eraser and erase objects it touches
    while True:
        mouse_x = win.getMouse().getX()
        mouse_y = win.getMouse().getY()
        
        eraser.move(mouse_x - last_click_x, mouse_y - last_click_y)  # Move the eraser
        
        # Erase anything the eraser overlaps
        erase_objects(win, eraser)
        
        time.sleep(0.05)

if __name__ == '__main__':
    main()
