class balance:
    def __init__(self,amount, last_interest):
        self.amount = amount
        self.interest = last_interest

    def __str__(self):
        return f'{self.amount} and {self.interest}'

    # __add__ is like overloading + operator in c++.
    # you need to define behavriour of the sum operation when two instance of this class get added
    def __add__(self, rhs):
        self.amount = self.amount + rhs.amount
        self.interest = max(self.interest, rhs.interest)
        return self

b1 = balance(456,3)
b2 = balance(1788, 4)

bresult = b1 + b2
print(bresult) #2244 and 4
