# The point of this code is to create the coordinates of the obstacles that the 
# simulated robot will navigate through.

# Set map dimensions to 100 to 200
# have 10 obstacles, and 30 pot holes
# set the mining site as necessary
# need 12 set of lists of coordinates of obstacles as well as the type of obstacle, 8 passable ones, and 4 unpassable ones

# To create a list of coordinates of humps, potholes, craters
from numpy import random
#from matplotlib import pyplot as plotter

#def plotItNow(list):
def format(list):
  sdf = 0# this function will format the output into the text file

def intoFile(list, type):
  file = open("Coordinate_List.txt", "a")
  # out the dman code in which will deal with the file wrigint
  # Type will tell us which kinda list it is, like if it is possible to get through it or not
  list = format(list)
  if type == "Boulder":
    file.writelines("Boulder Coordinates:\n")
    file.writelines(list)
  if type == "Pothole":
    file.writelines("Pothole Coordinates:\n")
    file.writelines(list)
  if type == "Crater":
    file.writelines("Crater Coordinates:\n")
    file.writelines(list) 
  file.close()

# THis class is where the obstacles are generated
class Obstacle:  
  class Pothole:
    def __init__(self, XY):
      self.z = (-1) * random.randint(0, 5)
      self.XY = XY
      self.safety_rad = 2

  class Crater:
    def __init__(self, XY):
      self.z = - 40
      self.XY = XY
      self.safety_rad = 20

  class Boulders:
    def __init__(self, XY):
      self.z = 15
      self.XY = XY
      self.safety_rad = 45

  def __init__(self):
    self.obst_list = []
    pass

class generator:
  def __init__(self,XY,seed):
    self.XY = 0
    self.seed = 0

  class blocked:
    def geN1(seed):
      for i in range

  class free:
    def geN2(seed):

  def__init__(self):
  self.obst_list = []
  pass
      


# Use a class to call the methods that will randomly generate the obstacles used
# Takes in type of maps wanted 
# I need to figure out how to randomize the XY positions
random.seed(7)
list = []
for i in range(29):
    A = Obstacle.Pothole([random.randint(15,20), random.randint(3,35)])
    list.append([A.XY, A.safety_rad])

generator("Blocked")


#print(list)
#print("sifuisdbgsnignsdignousdnogn")
#print(str(list))