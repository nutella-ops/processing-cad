#GLOBAL
one = 100 #one drawing unit
rulerScale = 30

#DRAWING FUNCTIONS

#global scale ruler
def omniRuler(dim):
    return dim * 10 * 1/rulerScale

#local scale ruler
def ruler(s, dim):
    return dim * 10 * 1/s*10

#bisect x dimension of a rectangle or triangle
def midX(a, b):
    return abs(a+b)/2

#bisect y dimension of a rectangle or triangle
def midRecY(y1, y2):
    return abs(y1+y2)/2

#draw rectangle using its center as reference point
def rectRev(x, y, w, l):
    x=x-w/2
    y=y-l/2
    rect(x, y, w, l)

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

    
