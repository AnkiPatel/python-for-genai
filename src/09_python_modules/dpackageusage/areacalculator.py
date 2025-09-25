from math import pi as _pi
# Here we imported pi value from math libraray as private attribute
# _ makes attribute/method private

class rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    # below method will not be available for module user. It is private
    def _has_negative_val(self) -> bool:
        if(self.height < 1) or (self.width < 1):
            return True
        else:
            return False

    def area(self) -> float:
        area = 0;
        if(self._has_negative_val()):
            print("With negative measure, area cannot be calculated")
        else:
             area = self.height * self.width
        return area

class circle:
    def __init__(self, radius):
        self.radius = radius

    # below method will not be available for module user. It is private
    def _has_negative_val(self) -> bool:
        return self.radius < 1

    def area(self) -> float:
        area = 0;
        if(self._has_negative_val()):
            print("With negative measure, area cannot be calculated")
        else:
             area = _pi * self.radius**2
        return area

if __name__ == '__main__':
    # This only get executed when areacalculator.py get used as script
    r1 = rectangle(10,5)
    print(r1.area())
    r2 = rectangle(-3, 2)
    print(r2.area())
    c1 = circle(5)
    print(c1.area())