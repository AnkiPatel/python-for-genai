class RobotTwo:
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
        RobotTwo.population += 1

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

    '''
    You can introduce new attribute runtime (unlike c++ or java) during method call
    '''
    def setEnergy(self, energy):
        self.energy = energy


r1 = RobotTwo('aloha', 30)
r1.setEnergy(310)
print(r1) #Robot: aloha 30
print(r1.energy)
# Another way to get attribute value is to use dunder method 'getattr(attribute name)'
print(getattr(r1, 'energy'))
print(getattr(r1, 'country', 'N/A')) # case when you dont know if actully such attribute present. to exception you can set default value


'''
class attribute. it is shared accross all instances. They are like static varible in c++ and java
Normally they get placed right below of class header (class description)
'''

class Platform:
    """Platform on which robot can move"""
    grid_row_count = 10 # Class attribute
    gird_column_count = 4 # Class attribute

print(Platform.grid_row_count) # you need to use class name to access class attribute
