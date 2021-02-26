class Fixed:
    """Type arithmétique à point fixe."""
    def __init__(self, n):
        self.n = n
        multiplier = ''
        
        if '.' in str(n):
            numberOfZeroes = len(str(n).replace('.', '')) - str(n).index('.')
            multiplier = '1' + multiplier.zfill(numberOfZeroes)
            n = int(n * int(multiplier))
            self.multd = n
            self.bin = bin(n)
        else:
            self.bin = bin(int(n))

    def __add__(self, other):
        pass
        
    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

x = Fixed(12.1)
y = Fixed(12.11)
c = Fixed(3.855)

print(x.n, x.multd, x.bin, bin(121))
print(y.n, y.multd, y.bin, bin(1211))
print(c.n, c.multd, c.bin, bin(3855))
# print(y.bin, bin(1211))

# print(x.e, x.f)
# print(x.eBinaire, x.fBinaire)