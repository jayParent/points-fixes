# Jerome Parent 

# Python 3.8
# Pour lancer les tests, éxécuter le script 'fixed.py'

# Quels effets a la precision sur les iterations de l'algorithme de Newton?
# La précision très limitée de notre implémentation à 16 bits (seulement 4 bits pour la partie fractionnaire) resulte en l'obtention d'un résultat
# approximatif après peu d'itérations. Par contre, augmenter le nombre d'itérations ne nous permet pas
# de nous approcher de plus en plus du vrai zéro comme il sera le cas avec le même algoritme mais avec une plus
# grande précision. Sachant que le nombre de chiffres significatifs corrects double à chaque itération, n'utiliser que 4 bits
# limite très rapidement l'augmentation de précision à chaque itération.

test_list = [7, 15, 30, 36, 99]
iterations = 5
class Fixed:
    """Type arithmétique à point fixe sur 16 bits."""
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
            self.fraction = f'{int(fraction / (1 / 16)):04b}'

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
        return str(self.n) if not self.overflow else OverflowError

    def __add__(self, other):
        result = int(self.whole, 2) + int(other.whole, 2) + (int(self.fraction, 2) * (1 / 16)) + (int(other.fraction, 2) * (1 / 16))

        return Fixed(result)

    def __sub__(self, other):
        result = (int(self.whole, 2) + (int(self.fraction, 2) * (1 / 16))) - (int(other.whole, 2) + (int(other.fraction, 2) * (1 / 16)))
        
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
        print(f't{t}: {xt}')
        xt = newton(xt, n)
    
    print('**********************\n')

def tests(list, iterations):
    for t in list:
        newton_sqrt(t, iterations)

tests(test_list, iterations)

# Références
# https://inst.eecs.berkeley.edu/~cs61c/sp06/handout/fixedpt.html
# https://en.wikipedia.org/wiki/Fixed-point_arithmetic