# Pre-release materials
## Task 1
### task 1.1
JSP structure diagrams show the basic structure of the program and functions within it. Basic operations like comparisons and if statement are also shown.

### task 1.2
The * sign means an iteration takes place.
The o sign means a selection takes place between two conditions.

### task 1.3
```
NOT EOF
Salary > 50
Salary >= 90
"Project Manager."
"Lead Developer."
"Manager."
```

### task 1.4
Under the condition `Salary > 50` is `FALSE`, add a condition `Salary > 70` (with a selection sign on the corner). If TRUE, add an operation called "Assign Consultant"; if FALSE, go to selection 

### task 1.5
Add under line 9:
```
IF Salary > 70
	THEN Role <- "Consultant."
	ELSE Role <- "Lead Developer."
ENDIF
```
Delete line 9.

### task 1.6
```
def role(salary):
	s = salary
	role = ""
	if s > 50:
		if s >= 90:
			role = "Project Manager."
		elif s > 70:
			role = "Consultant."
		else:
			role = "Lead Developer."
	else:
		role =  "Manager."
	return role
```
---------------------------------------
---------------------------------------
---------------------------------------
## Task 2
### task 2.1
class Toy:
Attributes:
name
id
price
minimum_age

Functions:
setName()
setID()
setPrice()
setMinimumAge()
getName()
getID()
getPrice()
getMinimumAge()

class ComputerGame:
Attributes:
category
console

Functions:
setCategory()
setConsole()
getCategory()
getConsole()

class Vehicle:
Attributes:
type
height
length
weight

Functions:
setType()
setHeight()
setLength()
setWeight()
getType()
getHeight()
getLength()
getWeight()

### task 2.2
Inheritance means that the parameters of a class is passed directly to its subclasses.
In my class diagram, ComputerGame and Vehicle are subclasses of the Toy.

### task 2.3
```
class toy:
        def __init__(self, n, i, p, m):
            self.name = n
            self.id = i
            self.price = p
            self.minimumage = m
        
        def getName(self):
            return self.name
            
        def setName(self, name):
            self.name = name
            
        def getID(self):
            return self.id
        
        def setID(self,id):
            self.id = id
        
        def getPrice(self):
            return self.price
            
        def setPrice(self, price):
            self.price = price
        
        def getMinimumAge(self):
            return self.minimumage
       
       def setMinimumAge(self, age):
            self.minimumage = age

```

### task 2.4
```
class ComputerGame(Toy):
	def __init__(self, n, i, p, m, ct, cs):
		toy.__init__(self, n, i, p, m)
		self.category = ct
		self.console = cs

	def getCategory(self):
		return self.category

	def setCategory(self, category):
		self.category = category

	def getConsole(self):
		return self.console

	def setConsole(self, console):
		self.console = console


class Vehicle(Toy):
        def __init__(self, n, i, p, m, t, h, l, w):
            toy.__init__(self, n, i, p, m)
            self.type = t
            self.height = h
            self.weight = w
            self.length = l

       	def getType(self):
       		return self.type

       	def setType(self, type):
       		self.type = type

       	def getHeight(self):
       		return self.height

       	def setHeight(self, height):
       		self.height = height

       	def getWeight(self, weight):
       		return self.weight

       	def setWeight(self, weight):
       		self.weight = weight

       	def getLength(self):
       		return self.length

       	def setLength(self, length):
       		self.length = length
```

### task 2.5
```
try:
	if age > 0 and age < 18:
		self.age = age
	else:
		age = input("Pleas enter a new age.")

```

### task 2.6
vehicle = []
computerGame = []
vehicle.append("Red Sports Car", "RSC13", 15.00, 6, "car", 3.3, 12.1, 0.08)
computerGame.append("Player Unknowns's Battle Ground", ID = "PUBG13", 16.00, 13, "FPS", "Multiplayer")

### task 2.7
Under class Toy:
```
def printDetails(self, id = input("Please enter the ID of the toy.")
	print(self.name, self.id, self.price, self.minimumage)
```

### task 2.8
```
def discount(n):
        n = n/100
        for i in range(len(toy)):
            toy[i].prince = toy[i].price * n
```

### task 2.9
Bubble sort swaps the position of the values one by one; Insertion sort put the searched value into positions in the list until it finds the appropriate one.

### task 2.10
```
def sort():
        for i in range(1, len(Toys)):
            itemToBeInserted = toy[i]
            n = i-1
            while itemtobeinserted.price < toy[n].price and n > 0:
                toy[n+1] = toy[n]
                n -= 1
            toy[n+1] = itemToBeInserted
```
---------------------------------------
---------------------------------------
---------------------------------------
## Task 3
### task 3.1
character(habib).\s\s
character_type(habib, explorer).\s\s
has_skill(habib, timetravel).\s\s

animal(fish).\s\s
pet(habib, fish).\s\s

### task 3.2
pet(X, Y) if character(X) and animal(Y).

### task 3.3
character(candice).\s\s
character(andy).\s\s
character_type(candice, flowermaker).\s\s
character_type(andy, farmer).
skill(sweetflower).
skill(supermagnet).
animal(cat).
animal(dog).
pet(candice, cat).
pet(andy, dog).
has_skill(candice, sweetflower).
has_skill(andy, supermagnet).

### task 3.4
true.
X = princess.
X = jim.
X = invisibility.
X = jim.

### task 3.5
pet(jim, X).
has_skill(X, fly).
skill(X).
pet(X, Y) :-
	character_type(X, princess).
