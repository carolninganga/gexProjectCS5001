import graphicsPlus as gr
import sys

def main( argv ):
    # create a window 
    win = gr.GraphWin( "My window", 500, 500 )

    # print("argument1 ", argv[1])
    # create a circle
    c = gr.Circle( gr.Point ( 250, 250), 60 )

    # c.setFill( gr.color_rgb( 100, 30, 100 ) )
   

    # draw the circle inot the window 
    c.draw( win )
    # pause until user gets mouse
    win.getMouse()
    c.setFill( "green" )
    win.getMouse()
    c.move( 50, -40 )

    # pause to get the mouse again
    win.getMouse()
    win.close()

    return



if __name__ == "__main__":
    # if len(sys.argv) > 3:
        # print(sys.argv[1])
    main( [] )
