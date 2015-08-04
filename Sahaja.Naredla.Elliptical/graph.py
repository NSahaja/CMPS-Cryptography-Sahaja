"""
SahajaReddy Naredla
Cryptography - Program 3
Elliptical Curve
"""

import numpy as np
import matplotlib.pyplot as plt
import fractions

class plotTheGraph():
    #class initialization, initializes to the exact values given by the user from command prompt.
    def __init__(self,x1,y1,x2,y2,a,b):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.a = a
        self.b = b
        self.x3 = 0
        self.y3 = 0
        #finds the third point from the third point.
    def findPoint(self):        
        if (((self.y1**2) == ((self.x1**3) + (self.a*self.x1) + (self.b))) and ((self.y2**2) == ((self.x2**3) + (self.a*self.x2) + (self.b)))):
            m = 0
            if (self.y1 != self.y2):
                m = (self.y1 - self.y2)/(self.x1 - self.x2)        
            else:
                m = ((3*(self.x1**2))+self.a)/(2*self.y1)
                
            self.x3 = (m**2)- self.x1 - self.x2
            self.y3 = m*(self.x3 - self.x1) + self.y1
            print('The third point is (', fractions.Fraction(self.x3).limit_denominator(1000),',',fractions.Fraction(self.y3).limit_denominator(1000),')')
        else:
            print("Please give the points which are on the graph")
            exit   

        #Plots the graph when the three points are given.
    def drawGraph(self):
    
        #Values defining our curve
        a = self.a
        b = self.b
        
        # Create two points
        y2 = self.y2
        x3 = self.x3
        y3 = self.y3
        x1 = self.x1
        y1 = self.y1
        x2 = self.x2
    
        #Determines width and height of plot
        adjustGraph = max(abs(x1),abs(x2),abs(x3),abs(y1),abs(y2),abs(y3))
        w = adjustGraph+15
        h = adjustGraph+15
    
        # Annotate the plot with your name using width (w) and height (h) as your reference points.
        an1 = plt.annotate("SahajaReddy Naredla", xy=(-w+2 , h-2), xycoords="data",
                      va="center", ha="center",
                      bbox=dict(boxstyle="round", fc="w"))
    
        # This creates a mesh grid with values determined by width and height (w,h)
        # of the plot with increments of .0001 (1000j = .0001 or 5j = .05)
        y, x = np.ogrid[-h:h:1000j, -w:w:1000j]
    
        # Plot the curve (using matplotlib's countour function)
        # This drawing function applies a "function" described in the
        # 3rd parameter:  pow(y, 2) - ( pow(x, 3) - x + 1 ) to all the
        # values in x and y.
        # The .ravel method turns the x and y grids into single dimensional arrays
        plt.contour(x.ravel(), y.ravel(), pow(y, 2) - ( pow(x, 3) + a*x + b ), [0])
    
        #Get the slope of the line
        m = (y1-y2)/(x1-x2)
    
        # Plot the points ('ro' = red, 'bo' = blue, 'yo'=yellow and so on)
        plt.plot(x1, y1,'ro')
    
        # Annotate point 1
        plt.annotate('x1,y1', xy=(x1,y1), xytext=(x1+1,y1+1),
                arrowprops=dict(arrowstyle="->",
                connectionstyle="arc3"),
                )
    
        plt.plot(x2, y2,'ro')
    
        # Annotate point 2
        plt.annotate('x2,y2', xy=(x2,y2), xytext=(x2+1,y2+1),
                arrowprops=dict(arrowstyle="->",
                connectionstyle="arc3"),
                )
    
        # Use a contour plot to draw the line (in pink) connecting our point.
        plt.contour(x.ravel(), y.ravel(), (y-y1)-m*(x-x1), [0],colors=('pink'))
    
        # I hard coded the third point, YOU will use good old mathematics to find
        # the third point
        plt.plot(x3, y3,'yo')
    
        # Annotate point 3
        plt.annotate('x3,y3', xy=(x3,y3), xytext = (x3+1,y3+1),
                arrowprops=dict(arrowstyle="->",
                connectionstyle="arc3"),
                )
    
        # Show a grid background on our plot
        plt.grid()
    
        # Show the plot
        plt.show()
