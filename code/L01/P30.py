def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if (a < b):
        a,b = b,a
    while b != 0:
        a, b = b, a%b
    return a
    
#############################################################
class Rational(object): 
    def __init__(self, numer, denom = 1):
        assert denom != 0
        g = gcd(numer,denom)
        self.numer = numer//g
        self.denom = denom//g
        if self.denom < 0:
            self.numer, self.denom = -self.numer, -self.denom
            
    def __add__(self, r):
        if type(r) == int: r = Rational(r,1)
        return Rational(-100) # remove this after completion
        
    def __sub__(self, r):
        if type(r) == int: r = Rational(r,1)
        return Rational(-100) # remove this after completion
        
    def __mul__(self, r):
        if type(r) == int: r = Rational(r,1)
        return Rational(-100) # remove this after completion

    def __truediv__(self, r):
        if type(r) == int: r = Rational(r,1)
        assert r.numer != 0
        return Rational(-100) # remove this after completion

    def __neg__(self):  # unary minus
        return Rational(-100) # remove this after completion

    def __abs__(self):
        assert self.denom > 0
        return Rational(-100) # remove this after completion

    def __pow__(self, p):
        return Rational(-100) # remove this after completion

    def __radd__(self, r):  # to handle "sum = 0; sum = sum + Rational(1,2)"
        assert type(r) == int
        return Rational(-100) # remove this after completion
        
    def __rmul__(self, r):  # to handle "prod = 1; prod = prod * Rational(1,2)"
        assert type(r) == int
        return Rational(-100) # remove this after completion

    # https://portingguide.readthedocs.io/en/latest/comparisons.html
    def __eq__(self, r):
        if type(r) == int: r = Rational(r,1)  # to handle "Rational(1,2) == 1"
        return self.numer * r.denom == r.numer * self.denom

    def __ne__(self, r):
        if type(r) == int: r = Rational(r,1)  
        return None
        
    def __le__(self, r):
        if type(r) == int: r = Rational(r,1) 
        return None
        
    def __ge__(self, r):
        if type(r) == int: r = Rational(r,1) 
        return None
 
    def __lt__(self, r):
        if type(r) == int: r = Rational(r,1) 
        return None
       
    def __gt__(self, r):
        if type(r) == int: r = Rational(r,1) 
        return None
        
    def __str__(self):
        assert self.denom > 0
        if self.denom == 1: return str(self.numer)
        return str(self.numer) + "/" + str(self.denom)

######################################

def test():
    r1 = Rational(1,2)
    r2 = Rational(-4,-10)
    print(r1, r2)  # 1/2  2/5
       
    print(r1+r2)  # 9/10  
    print(r2-r1)  # -1/10
           
    r3 = Rational(2)
    r4 = Rational(7,5)
    print(r3 + r4 * (r1 + r2 * r2))  # 731/250
    print(r1 / r2)  # 5/4

    r5 = -r2
    print(r5, r2)  # -2/5  2/5
    print(-r5)     # 2/5

    print(abs(r5), r5)  # 2/5  -2/5

    print(r5**4)  # 16/625

    sum = 0
    for i in range(5):
        sum = sum + r2  # __radd__ is called at 1st iteration
        sum += r1
    print(sum)  # 9/2

    prod = 1
    for i in range(6):
        prod = prod * r2  # __rmul__ is called at 1st iteration
        prod *= (-1)**i * r1
    print(prod)  # -1/15625
    
    print(-r1 > 0, r1 > -1)   # False True
    print(r1 == r1, r1 != r1, r1 <= r1, r1 >= r1, r1 < r1, r1 > r1)
    # True False True True False False
    print(r1 == r2, r1 != r2, r1 <= r2, r1 >= r2, r1 < r2, r1 > r2)
    # False True False True False True

if __name__ == '__main__': test()
