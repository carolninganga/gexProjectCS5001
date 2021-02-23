# Caroline Ninganga
# CS 5001
# Zelle Graphics first example

import graphicsPlus as gr
import sys

def main( argv ):
    # create a window 
    win = gr.GraphWin( "My window", 500, 500 )

    print("argument1 ", argv[1])
    # create a circle
    c = gr.Circle( gr.Point ( int(argv[2]), int(argv[3])), int(argv[1]))

    c.setFill( gr.color_rgb( 100, 30, 100 ) )
   

    # draw the circle inot the window 
    c.draw( win )

    # pause until user gets mouse
    win.getMouse()
    win.close()

    return



if __name__ == "__main__":
    if len(sys.argv) > 3:
        # print(sys.argv[1])
        main( sys.argv )

