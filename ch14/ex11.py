#parent class
class Animal:
    def __init__(self, name, age, gender, colour):
        #define instance variables and assign them with values
        self.name = name
        self.age = age
        self.gender = gender
        self.colour = colour
    def move(self):
        #print moving
        print('moving')
    def make_sound(self):
        #print sound
        print('sound')

    def breathe(self): 
        #print breathing
        print('breathing')


#extending parent class
class Dog(Animal):
    def __init__(self, name, age, gender, colour):
        #define the instance variables and assign them with values
        self.name = name
        self.age = age
        self.gender = gender
        self.colour = colour

    #extending the parent class
    def run(self):
        #print running
        print('running')

#instantiate the object
dog = Dog('Jacky', 3, 'Male', 'Brown')

#accessing the methods of the parent class
dog.move()
dog.make_sound()
dog.breathe()

#Accessing the run() method defined in the child class
dog.run()

# Overriding parent class
class Dog(Animal):
    def __init__(self, name, age, gender, colour):
        #define the instance variables and assign them with values
        self.name = name
        self.age = age
        self.gender = gender
        self.colour = colour

    #overidding the parent class
    def move(self):
        print('run run run...')
    def make_sound(self):
        print('bark bark bark..')
#instantiate the object
dog = Dog('Jacky', 3, 'Male', 'Brown')

#accessing the overridden methods
dog.move()
dog.make_sound()

