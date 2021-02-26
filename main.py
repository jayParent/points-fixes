class Fixed:
    """Type arithmétique à point fixe."""
    def __init__(self, n):
        self.n = n
        # Partie entiere
        self.e = str(n).split('.')[0]
        self.eBinaire = bin(int(self.e))
        # Partie fractionnaire
        try:
            self.f = str(n).split('.')[1]
            self.fBinaire = bin(int(self.f))      
        except:
            pass

    def __add__(self, other):
        if type(self.n == int and type(other.n == int)):
            e = int(self.eBinaire, 2) + int(other.eBinaire, 2)
            return e
        else:
            e = int(self.eBinaire, 2) + int(other.eBinaire, 2)
            f = int(self.fBinaire, 2) + int(other.fBinaire, 2)
            return Fixed(e) + Fixed(f)
        
    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __truediv__(self, other):
        pass

x = Fixed(12.1)
y = Fixed(10)
sum = x + y
print(sum)
# print(x.e, x.f)
# print(x.eBinaire, x.fBinaire)