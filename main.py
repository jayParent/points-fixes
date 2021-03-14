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
        point_index = self.point_index if self.point_index > other.point_index else other.point_index

        result = int(self.bin, 2) + int(other.bin, 2)
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

x = Fixed(53)
y = Fixed(26.5)
c = x + y
print(x.bin)
print(y.bin)
# print(f'{x}, shifts: {x.shifts}')
# print(f'{y}, shifts: {y.shifts}')