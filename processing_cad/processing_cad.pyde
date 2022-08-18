#DIMENSION FUNCTIONS

#metric
def cm(dim):
    return dim * 64.625 #4k screen
    # formerly 58.0, macbook screen

def m(dim):
    return cm(dim)*100.0

def km(dim):
  return m(dim)*1000.0

def inch(dim):
  return cm(2.54*dim)


#DRAWING FUNCTIONS

#scale ruler
def ruler(s, dim):
    return dim * 10 * 1/s*10

def omniRuler(dim):
    return dim * 10 * 1/rulerScale

#MAIN PROGRAM
# def setup():
size(1600,2000)
frameRate(1)



# def draw():
# for s in [1, 2, 3, 4, 5]:
#     rect(inch(0.5), inch(1), ruler(s, inch(8)), ruler(s, inch(5)))

rect(inch(0.1), inch(0.1), inch(2), inch(11.8))
   

     
