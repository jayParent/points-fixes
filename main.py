# Pour lancer les tests, éxécuter le script 'main.py'
test_list = [7, 15, 30, 36, 99]
iterations = 5
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
        return str(self.n)

    def __add__(self, other):
        result = int(self.whole, 2) + int(other.whole, 2) + (int(self.fraction, 2) * 0.0625) + (int(other.fraction, 2) * 0.0625)

        return Fixed(result)

    def __sub__(self, other):
        result = (int(self.whole, 2) + (int(self.fraction, 2) * 0.0625)) - (int(other.whole, 2) + (int(other.fraction, 2) * 0.0625))
        
        return Fixed(result)

    def __mul__(self, other):
        factor = self.shifts + other.shifts
        result = (int(self.bin.replace('.', ''), 2) * int(other.bin.replace('.', ''), 2)) * (2 ** -factor)
        
        return Fixed(result)

    def __truediv__(self, other):
        factor = self.shifts + other.shifts
        result = (int(self.bin.replace('.', ''), 2) / int(other.bin.replace('.', ''), 2)) 

        return Fixed(result)

def newton(xt, n):
    xtp1 = Fixed(0.5) * (xt + (Fixed(n) / xt))
    return Fixed(xtp1)

def newton_sqrt(n, iterations):
    print('**********************')
    print(f'Methode de Newton: sqrt({n})')
    xt = Fixed(0.5 * n)

    for t in range(iterations):
        xt = newton(xt, n)
        print(f't{t}: {xt}')
    
    print('**********************\n')

def tests(list, iterations):
    for t in list:
        newton_sqrt(t, iterations)

tests(test_list, iterations)