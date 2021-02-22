# Caroline Ninganga
# CS 5001
# Zelle Graphics first example

import graphicsPlus as gr

def main( argv ):
    # create a window 
    win = gr.GraphWin( "My window", 500, 500 )

    # create a circle
    c = gr.Circle( gr.Point ( 250, 250), 10 )

    # draw the circle inot the window 
    c.draw( win )

    # pause until user gets mouse
    win.getMouse()
    win.close()

    return

if __name__ == "__main__":
    main( [] )

