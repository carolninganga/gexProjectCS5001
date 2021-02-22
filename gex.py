# Caroline Ninganga
# CS 5001
# Zelle Graphics first example

import graphicsPlus as gr

def main( argv ):
    # create a window 
    win = gr.GraphWin( "My window", 500, 500 )

    # pause until user gets mouse
    win.getMouse()
    win.close()

    return

if __name__ == "__main__":
    main( [] )

