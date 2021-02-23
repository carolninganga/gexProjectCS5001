# Caroline Ninganga
# CS 5001
# Zelle Graphics first example
#
# rocket ship

import graphicsPlus as gr

def init_rocket(x, y, scale):
    # define the rocket shapes here and put them in a list

    #Body: Create a Rectangle using points (x-scale*10, y) and (x+scale*10, y-scale*80). 
#Set the Rectangle fill color to be a grey color (185, 185, 185).
    body = gr.Rectangle( gr.Point ( x-scale*10, y), gr.Point (x+scale*10, y-scale*80 ))
    body.setFill( gr.color_rgb( 185, 185, 185 ))

#Nose: Create a Polygon, with points (x-scale*10, y-scale*80), (x, y-scale*100 ), and (x+scale*10, y-scale*80 ). 
#Set the Polygon fill color to be a grey-blue color (150, 170, 200 ).

#L Fin: Create a Polygon, with points (x-scale*10, y), (x-scale*10, y-scale*20 ), and (x- scale*25, y+scale*5 ). 
#Set the Polygon fill color to be a grey-red color (200, 170, 150 ).

#R Fin: Create a Polygon, with points (x+scale*10, y), (x+scale*10, y-scale*20 ), and (x+scale*25, y+scale*5 ). 
#Set the Polygon fill color to be a grey-red color (200, 170, 150 ).
    return [body]

def main():
    # Create a GraphWin window that is at least 400 x 400
    win = gr.GraphWin( "My window", 400, 400 )

    # This part can cause issues. Remember that the return value of this function
    # IS A LIST CONTAINING ZELLE SHAPE OBJECTS NOT PYTHON OBJECTS.
    # assign to rocket1 the result of calling init_rocket with arguments 100, 300, 1
    rocket1 = gr.init_rocket( 100, 300, 1)

    # Look up python for each loops
    # for each shape in rocket1
        # draw the shape into the window
        
    body.draw( win )

    # wait for a mouse click
    win.getMouse()
    # close the window
    win.close()

    return

if __name__ == "__main__":
    main()