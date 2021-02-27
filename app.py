class Fixed:
    """Type arithmétique à point fixe."""

    def __init__(self, n):
        self.n = n
        multiplier = ''

        if '.' in str(n):
            self.point_index = str(n).index('.')
            number_of_zeroes = len(str(n).replace('.', '')) - self.point_index
            multiplier = '1' + multiplier.zfill(number_of_zeroes)
            n = int(n * int(multiplier))
            self.multd = n
            self.bin = bin(n)
        else:
            self.bin = bin(int(n))

    def __add__(self, other):
        point = self.point_index if self.point_index > other.point_index else other.point_index

        sum = int(self.bin, 2) + int(other.bin, 2)
        sum = str(sum)[:point] + '.' + str(sum)[point:]
        return float(sum)

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass


x = Fixed(411.1)
y = Fixed(1231.1)
c = Fixed(3.855)
a = Fixed(122)

sum = x + y
print(type(sum))

# print(x.n, x.bin)
# print(y.n, y.bin)
# print(c.n, c.bin)
# print(a.n, a.bin)
