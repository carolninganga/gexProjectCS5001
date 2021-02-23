import graphicsPlus as gr
import sys

import random

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
    win.getMouse() # pause
    c.setFill( "green" )  
    win.getMouse() 
    c.move( 50, -40 )
    c.undraw()

    # pause to get the mouse again
    win.getMouse()
    win.close()

    return

def interactive():

    win = gr.GraphWin( 'interactive demo', 500, 500 )
    r = gr.Rectangle( gr.Point( 220, 260 ), gr.Point( 280, 240 ))
    r.setOutline( 'purple')
    r.setFill( 'pink')
    r.setWidth( 3 )
    r.draw( win )

    counter = 0
    falling = None
    # begin event loop
    while True: #infinite loop

        if counter % 80 == 0:
            if falling != None:
                falling.undraw()
            falling = gr.Circle( gr.Point( random.randint(0, 500), 0 ), 10)
            falling.setFill( 'blue')
            falling.draw(win)
        
        if falling != None:
            falling.move( random.randint(-3, 3), 5 )

            counter += 1


        key = win.checkKey()
        if key == 'q':
            break
        elif key == 'a': #move left
            r.move( -20, 0 )
        elif key == 'w': #move up
            r.move( 0, -20 )
        elif key == 's': #move down
            r.move( 0, 20 )
        elif key == 'd': #move right
            r.move( 20, 0 )

    win.getMouse()
    win.close()



if __name__ == "__main__":
    # if len(sys.argv) > 3:
        # print(sys.argv[1])
        interactive()
    # main( [] )
