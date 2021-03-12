class Fixed:
    """Type arithmétique à point fixe."""

    def __init__(self, n):
        self.n = n
        self.multiplier = ''

        if '.' in str(n):
            self.point_index = str(n).index('.')
            self.shifts = len(str(n).replace('.', '')) - self.point_index
            self.multiplier = '1' + self.multiplier.zfill(self.shifts)
            n = int(n * int(self.multiplier))

            self.bin = bin(int(n))
        else:
            self.point_index = len(str(n))
            self.shifts = 0
            self.bin = bin(n)
    
    def __str__(self):
        return str(self.n)

    def __add__(self, other):
        result = int(self.bin, 2) + int(other.bin, 2)
        print(int(self.bin, 2)) #?????
        print(result) #???????
        point_index = len(str(result)) - self.shifts - other.shifts

        result = str(result)[:point_index] + '.' + str(result)[point_index:]

        return Fixed(float(result))

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        result = (int(self.bin, 2) * int(other.bin, 2))
        point_index = len(str(result)) - self.shifts - other.shifts

        result = str(result)[:point_index] + '.' + str(result)[point_index:]

        return Fixed(float(result))

    def __truediv__(self, other):
        pass

x = Fixed(10.1)
y = Fixed(100)
c = x + y
print(c)
# print(f'{x}, shifts: {x.shifts}')
# print(f'{y}, shifts: {y.shifts}')