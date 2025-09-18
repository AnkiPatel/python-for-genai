# In python, class name follows rule of "Pascal case". First letter of the class should be capital


class Robot:
    """
    Class Dscription
    whatever you write here, will apear when someone perform __doc__ method.
    """

    population = 0 # Class attribute:  to track the number of Robot instances

    # For class it is optional to implement dunder methods.
    # __init__ is the dunder method. It is like "constructor" in Java and c++
    # while implementing dunder methods, you have to explicitly pass the caller's object, 'self'
    def __init__(self, name, price):
        self.name = name # name will be the class attrinute
        self.price = price  # price is also an attribute
        #NOTE: unlike c++ and java, you don't need to declare attributes in advance
        Robot.population += 1

    # __str__ is the dunder method. it will convert object into string.
    # like "toString" method in Java or overloading << operator in c++
    def __str__(self):
        return f'Robot: {self.name} {self.price}'

    '''
    In Python, destructors aka finalizers are less used, because python has a garbage
    collector that handles memory management. 
    '''
    def __del__(self):
        print(f'Object is getting deleted: {self.name}')


r1 = Robot('aloha', 30)
print(r1.__doc__) #It will show the class description
print(r1) #Robot: aloha 30

destScope = True
if destScope:
    r2 = Robot('suka', 31)
    print(r2)
print("out of if")

