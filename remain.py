class Fixed:
    """Type arithmétique à point fixe."""

    def __init__(self, n):
        self.n = n

        try:
            split_number = str(n).split('.')

            self.whole = bin(4096) if len(bin(int(split_number[0]))) > 12 else bin(int(split_number[0]))

        except:
            self.whole = bin(4096) if len(bin(int(n))) > 12 else bin(int(n))
            # self.fraction = bin(0)

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

x = Fixed(4097.1142)
y = Fixed(100)
c = x + y
print(x.whole)
print(y.whole)
# print(f'{x}, shifts: {x.shifts}')
# print(f'{y}, shifts: {y.shifts}')