class Fixed:
    """Type arithmétique à point fixe."""

    def __init__(self, n):
        self.n = n
        self.factor = ''

        if '.' in str(n):
            self.point_index = str(n).index('.')
            self.shifts = len(str(n).replace('.', '')) - self.point_index
            self.factor = int('1' + self.factor.zfill(self.shifts))
            n = int(n * self.factor)

            self.int = int(n)
        else:
            self.int = int(n)
        

    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        factor = self.factor * other.factor
        result = (self.int * other.int) / factor

        return Fixed(result)

    def __truediv__(self, other):
        pass

x = Fixed(26.5)
y = Fixed(26.55)
c = x * y
print(x)
print(y)
print(c)

# print(f'{x}, shifts: {x.shifts}')
# print(f'{y}, shifts: {y.shifts}')