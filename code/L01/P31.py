import copy
from P30 import Rational

class Matrix(object):
    def __init__(self, L):
        self.a = copy.deepcopy(L)

    def __str__(self):
        s = ""
        m,n = self.dim()
        for i in range(m):
            for j in range(n):
                if type(self.a[i][j]) == float:
                    s += str(round(self.a[i][j],5)) + " "
                else:
                    s += str(self.a[i][j]) + " "
            s += "\n"
        return s

    def dim(self): return (len(self.a), len(self.a[0]))

    def __add__(self, M):
        m,n = self.dim()
        p,q = M.dim()
        assert m == p and n == q
        A = Matrix(self.a)
        return Matrix([[-100]*n for i in range(m)]) # remove this after completion

    def __sub__(self, M):
        m,n = self.dim()
        p,q = M.dim()
        assert m == p and n == q
        return Matrix([[-100]*n for i in range(m)]) # remove this after completion

    def __mul__(self, M):
        m,p = self.dim()
        q,n = M.dim()
        assert p == q
        return Matrix([[-100]*n for i in range(m)]) # remove this after completion

    def __pow__(self, b):
        assert b > 0
        m,n = self.dim()
        assert m == n
        # fast exponentiation by recursion
        if b == 1:
            return self
        else:
            return Matrix([[-100]*n for i in range(m)]) # remove this after completion

    def __rmul__(self, factor): # used for scalar multiplication (factor * self)
        m,n = self.dim()
        return Matrix([[-100]*n for i in range(m)]) # remove this after completion

    def transpose(self):
        m,n = self.dim()
        return Matrix([[-100]*m for i in range(n)]) # remove this after completion
        
    def submatrix(self, i, j):
        m,n = self.dim()
        assert m>=2 and n>=2 and 0<=i<m and 0<=j<n
        return Matrix([[-100]*(n-1) for i in range(m-1)]) # remove this after completion

    def determinant(self):
        m,n = self.dim()
        assert m == n
        if n == 1:
            return self.a[0][0]

        # Laplace expansion
        return -1  # remove this after completion

    def inverse(self):
        m,n = self.dim()
        assert m == n
        return Matrix([[-100]*m for i in range(n)]) # remove this after completion

#################################################################
def test():
    A = Matrix( [ [1,2,3], [4,5,6] ] )
    B = Matrix( [ [10,11,12], [13,14,15] ] )
    C = Matrix( [ [7,8], [9,10], [11,12] ] )
    D = Matrix( [ [1,0,0], [0,-1,0], [0,0,-1] ] )
    E = Matrix( [ [1,2,3,4], [5,3,7,8], [9,2,6,8], [8,7,13,7] ] )

    print(A+B-A+B)
    # 20 22 24
    # 26 28 30

    print(A*C)
    # 58 64 
    # 139 154
    print(C*A)
    # 39 54 69 
    # 49 68 87 
    # 59 82 105

    print(D**1012398123643612637943908129)
    # 1  0  0
    # 0 -1  0
    # 0  0 -1

    print(A.transpose())
    # 1 4
    # 2 5
    # 3 6
    
    print(-3*A)
    #  -3  -6  -9 
    # -12 -15 -18

    print(E.submatrix(2,1))
    # 1  3 4 
    # 5  7 8 
    # 8 13 7

    print(E.determinant())
    # -179

    print(E.inverse())
    # 0.11173 -0.34637 0.2514 0.04469 
    # 1.39106 -1.21229 0.37989 0.15642 
    # -0.94413 0.82682 -0.3743 0.02235 
    # 0.23464 0.07263 0.02793 -0.10615

    L = [[None]*4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            L[i][j] = Rational(E.a[i][j])

    F = Matrix(L)
    print(F.inverse())
    #   20/179  -62/179  45/179   8/179 
    #  249/179 -217/179  68/179  28/179 
    # -169/179  148/179 -67/179   4/179 
    #   42/179   13/179   5/179 -19/179
    
test()