class Animal(object):
  """Makes cute animals."""
  is_alive = True
  health = 'good'
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)
    
    
hippo = Animal('Mike', 24)
hippo.description()

sloth = Animal("jiji", 44)
ocelot = Animal("Laifu", 20)

print(hippo.health)
print(sloth.health)
print(ocelot.health)


#-----------------------------------------

class ShoppingCart(object):
  """Creates shopping cart objects
  for users of our fine website."""
  
  def __init__(self, customer_name):
    self.customer_name = customer_name
    self.items_in_cart = {}
  def add_item(self, product, price):
    """Add product to the cart."""
    if not product in self.items_in_cart:
      self.items_in_cart[product] = price
      print product + " added."
    else:
      print product + " is already in the cart."

  def remove_item(self, product):
    """Remove product from the cart."""
    if product in self.items_in_cart:
      del self.items_in_cart[product]
      print product + " removed."
    else:
      print product + " is not in the cart."
my_cart = ShoppingCart("Mike")
my_cart.add_item("cereal", 45)

# ----------------------------------------------

class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  
  def calculate_wage(self, hours):
    self.hours = hours
    
    return hours*12.00
  
temp = PartTimeEmployee("lucy")
worker = Employee("Laifu")

print(worker.calculate_wage(20))
print(temp.calculate_wage(30))

# 400
# 360
  

    
  


# ----------------------------------------------
class Employee(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

# Add your code below!
class PartTimeEmployee(Employee):
  
  def calculate_wage(self, hours):
    self.hours = hours
    
    return hours*12.00
  
  def full_time_wage(self, hours):
    
    return super(PartTimeEmployee, self).calculate_wage( hours)
  
  
  
temp = PartTimeEmployee("lucy")
worker = Employee("Laifu")

print(worker.calculate_wage(20))
print(temp.calculate_wage(30))

milton= PartTimeEmployee("milton")
print(milton.full_time_wage(10))

# 400
# 360
# 200


# ------------------example-----------------------


class Triangle(object):
  
  number_of_sides = 3 
  
  def __init__(self,angle1, angle2, angle3):
    
    self.angle1 = angle1
    self.angle2 = angle2
    self.angle3 = angle3
    
  def check_angles(self):
    
    if (self.angle1 + self.angle2 + self.angle3 == 180) :
      return True
    else:
      return False
    
class Equilateral(Triangle):
  angle = 60
  
  def __init__(self):
    self.angle1= self.angle
    self.angle2= self.angle
    self.angle3= self.angle
    
  
my_triangle =  Triangle(90,30,60)

print(my_triangle.number_of_sides)

print(my_triangle.check_angles())



# -------------------------------------------

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))

my_car = Car("DeLorean", "silver", 88)

my_car.display_car()


#----------------------------------------------

class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"

my_car = Car("DeLorean", "silver", 88)

print my_car.condition
my_car.drive_car()
print my_car.condition



# ----------------------------------------------


class Car(object):
  condition = "new"
  def __init__(self, model, color, mpg):
    self.model = model
    self.color = color
    self.mpg   = mpg
   
  def display_car(self):
    print "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg))
    
  def drive_car(self):
    self.condition = "used"
    
    
class ElectricCar(Car):
  
  def __init__(self, model, color, mpg, battery_type):
    self.model = model
    self.color = color
    self.mpg   = mpg
    self.battery_type = battery_type
    
  def  drive_car(self):
    self.condition = "like new"
    
    

my_car =  ElectricCar("DeLorean", "silver", 88, "molten salt")
print(my_car.condition)

my_car.drive_car()

print(my_car.condition)


# new
#like new



#One useful class method to override is the built-in __repr__() method, which is short for representation; by providing a return value in this method, we can tell Python how to represent an object of our class (for instance, when using a print statement)



class Point3D(object):
  
  def __init__(self, x, y, z):
    
    self.x = x
    self.y = y
    self.z = z
    
  def __repr__(self):
    
    return "(%d, %d, %d)" % (self.x, self.y, self.z)
  
my_point = Point3D(1,2,3)
print(my_point)

# (1, 2, 3)