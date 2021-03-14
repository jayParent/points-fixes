class Fixed:
    """Type arithmétique à point fixe."""

    def __init__(self, n):
        self.n = n
        factor = ''

        try:
            self.point_index = str(n).index('.')
            split_number = str(n).split('.')

            whole = f'{int(split_number[0]):012b}'
            self.whole = bin(0)[2:] if len(whole) > 12 else whole
            self.overflow = True if len(whole) > 12 else False

            factor = '1' + factor.zfill(len(split_number[1]))
            fraction = int(split_number[1]) / int(factor)
            self.fraction = f'{int(fraction / 0.0625):04b}'

            self.shifts = len(self.fraction)
            self.bin = f'{self.whole}.{self.fraction}'

        except:
            self.point_index = 0
            self.shifts = 0

            whole = f'{int(n):012b}'
            self.whole = bin(0)[2:] if len(whole) > 12 else whole
            self.overflow = True if len(whole) > 12 else False

            self.fraction = f'{0:04b}'

            self.shifts = len(self.fraction)
            self.bin = f'{self.whole}.{self.fraction}'

    def __str__(self):
        return str(f'{self.bin} ({self.n})') if self.overflow == False else str(f'{self.bin} ({OverflowError}) ({self.n})')

    def __add__(self, other):
        result = int(self.whole, 2) + int(other.whole, 2) + (int(self.fraction, 2) * 0.0625) + (int(other.fraction, 2) * 0.0625)

        return Fixed(result)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        shifts = self.shifts + other.shifts
        result = (int(self.bin.replace('.', ''), 2) * int(other.bin.replace('.', ''), 2)) * (2 ** -shifts)
        
        return Fixed(result)

    def __truediv__(self, other):
        pass

x = Fixed(10)
y = Fixed(10.5)
c = x + y
print(c)
# print(f'{x}, shifts: {x.shifts}')
# print(f'{y}, shifts: {y.shifts}')