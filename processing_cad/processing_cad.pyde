#GLOBAL
one = 100 #one drawing unit
rulerScale = 30

#DRAWING FUNCTIONS

class rectangle(): 
    def __init__(self):
        self.wid = w
        self.len = l
        self.widHalf = w/2
        self.lenHalf = l/2
        self.xPos = x
        self.yPos = y
        self.midX = abs(x+widHalf-x-widHalf)
    
    #draw rectangle using its center as reference point
    def reverse(self):
        return rect(xPos-widHalf, yPos-lenHalf, w, l)
        
    # #bisect y dimension of a rectangle or triangle
    # def midRecY(self):
    #     return abs(x)


class ruler():
    #global scale ruler
    def global(dim):
        return dim * 10 * 1/rulerScale
    
    #local scale ruler
    def local(s, dim):
        return dim * 10 * 1/s*10







#MAIN PROGRAM
size(1600,2000)

c=1714
m=800
b=1100
j=285

centX=midX(800, 1100)
centY=midRecY(1714, 285)
triangle(m, c, b, c, m, j)
rectRev(centX, centY, 150, 400)
line(centX, 0, centX, height)
line(0, centY, width, centY)





# triangle(x, y, omniRuler(dimX), omniRuler(dimY))

    
