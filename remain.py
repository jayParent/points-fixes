class Fixed:
    """Type arithmétique à point fixe."""

    def __init__(self, n):
        self.n = n
        factor = ''

        try:
            self.point_index = str(n).index('.')
            split_number = str(n).split('.')

            self.whole = bin(4096) if len(bin(int(split_number[0]))) > 12 else bin(int(split_number[0]))
            self.whole = self.whole[2:]

            factor = '1' + factor.zfill(len(split_number[1]))
            fraction = int(split_number[1]) / int(factor)
            self.fraction = bin(int(fraction / 0.0625))[2:]

            self.shifts = len(self.fraction)
            self.bin = f'{self.whole}.{self.fraction}'

        except:
            self.point_index = 0
            self.shifts = 0

            self.whole = bin(4096) if len(bin(int(n))) > 12 else bin(int(n))
            self.whole = self.whole[2:]

            self.fraction = bin(0)[2:]

            self.shifts = len(self.fraction)
            self.bin = f'{self.whole}.{self.fraction}'

    def __str__(self):
        return str(f'{self.bin} ({self.n})')

    def __add__(self, other):
        if self.shifts > other.shifts:
            difference = self.shifts - other.shifts
            print(other.bin)
            other.bin = other.bin.replace('.', '')
            other.bin = f'{other.bin[:difference]}.{other.bin[difference:]}'
            print(other.bin)


        # return Fixed(result)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        shifts = self.shifts + other.shifts
        result = (int(self.bin.replace('.', ''), 2) * int(other.bin.replace('.', ''), 2)) * (2 ** -shifts)
        
        return Fixed(result)

    def __truediv__(self, other):
        pass

x = Fixed(8.5)
y = Fixed(4)
c = x + y
# print(f'{x}, shifts: {x.shifts}')
# print(f'{y}, shifts: {y.shifts}')