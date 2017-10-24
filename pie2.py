import math
import random

name = "PIE"
class Pastry():
  name = "PIE"
  def __init__(self, name, ingredients):
    self.name = name
    self.ingredients = ingredients

  def getCost(self, markup = 0.33 ):
    total = 0

    for ingredient in self.ingredients:
      total = total + ingredient.cost

    total = total + total * markup
    return math.ceil(total)

class CostedItem():
  def __init__(self, name, cost):
    self.name = name
    self.cost = cost

piecrust = CostedItem("piecrust", 3.00)
butter = CostedItem("butter", 1.50)
eggs = CostedItem("eggs", 0.50)
decoration = CostedItem("decoration", 2.50)
whippedcream = CostedItem("whippedcream", 0.75)
pumpkin = CostedItem("pumpkin", 1.50)
pecan = CostedItem("pecan", 1.25)
apple = CostedItem("apple", 0.75)
starberry = CostedItem("starberry",0.75)
blueberry = CostedItem("blueberry",0.75)
sugar = CostedItem("sugar",1.75)

piez = [
  Pastry("Pecan pie", [piecrust, butter, eggs, whippedcream, sugar, pecan]),
  Pastry("Pumpkin pie", [piecrust, butter, eggs, whippedcream,sugar, pumpkin]),
  Pastry("Starberry pie", [piecrust, butter,eggs, whippedcream, sugar, starberry]),
  Pastry("Apple pie", [piecrust, butter, eggs, whippedcream,sugar, apple]),
  Pastry("Blueberry pie", [piecrust, butter, eggs, whippedcream, sugar, blueberry]),
  Pastry("Fancy pecan pie", [piecrust, butter, eggs, whippedcream, pecan, sugar, decoration]),
  Pastry("Fancy pumpkin pie", [piecrust, butter, eggs,  whippedcream, pecan, sugar, decoration]),
  Pastry("Fancy starberry pie", [piecrust, butter,eggs, whippedcream, starberry, sugar, decoration]),
  Pastry("Fancy blueberry pie", [piecrust, butter, eggs, whippedcream, blueberry, sugar, decoration])
]

p = ["Pecan pie","Pumpkin pie","Starberry pie","Apple pie", "Blueberry pie"]

order = random.choice(piez)

rpie = random.choice(piez)

sum = 0
for wich in piez:
  print (wich.name + " " + str(wich.getCost()))
  sum = sum + wich.getCost()

print ("TOTAL: " + str(sum))

print ("Would you like some " + str(order.name) + "?")
