# Caroline Ninganga
# CS 5001
# complex object example

import graphicsPlus as gr


# creates and returns a list of objects
# should be a beautiful whale with a city on top 

def citywhale( x, y, scale ):

    # define a polygon for the body
    bodylist = [ gr.Point( x + 5*scale, y - 5*scale ),
                 gr.Point( x + 25*scale, y - 2*scale ),
                 gr.Point( x + 45*scale, y - 8*scale ),
                 gr.Point( x + 70*scale, y - 15*scale ),
                 gr.Point( x + 100*scale, y - 6*scale ),
                 gr.Point( x + 90*scale, y - 20*scale ),
                 gr.Point( x + 100*scale, y - 34*scale ),
                 gr.Point( x + 80*scale, y - 25*scale ),
                 gr.Point( x + 55*scale, y - 27*scale ),
                 gr.Point( x + 45*scale, y - 30*scale ),
                 gr.Point( x + 24*scale, y - 27*scale ),
                 gr.Point( x + 8*scale, y - 24*scale ),
                 gr.Point( x - 8*scale, y - 25*scale ) ]
    whalebody = gr.Polygon( bodylist)
    whalebody.setFill( 'purple')
    whalebody.setOutline( 'darkblue' )
    whalebody.setWidth( 4 )

    # define a polygon for the mouth
    mouthlist = [ gr.Point( x + 24*scale, y - 27*scale ),
                 gr.Point( x + 8*scale, y - 24*scale ),
                 gr.Point( x - 8*scale, y - 25*scale ), 
                 gr.Point( x + 8*scale, y - 32*scale ) ]
    whalemouth = gr.Polygon( mouthlist )
    whalemouth.setFill( 'grey')
    whalemouth.setOutline( 'dark blue' )
    whalemouth.setWidth( 2 )
    
    # define four rectangles for the city

    # put all these objects into a list

    whale = [ whalebody, whalemouth ]

    # return the list

    return whale

def main():

    win = gr.GraphWin( 'whales', 1000, 1000 )

    # whale is a list of graphics objects
    whale = citywhale( 500, 500, 2.0 )

    #  draw each graphics object into the window
    for thing in whale:
        thing.draw( win )

    win.getMouse()
    win.close()

if __name__ == "__main__":
    main()


