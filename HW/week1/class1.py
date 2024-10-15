class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __str__(self):
        string = ""
        if (self.a!=0):
            string += str(self.a)
            if (self.b<0):
                string += str("-"+ str(-self.b)+ "i")
            elif (self.b>0) :
                string += str("+" + str(self.b) + "i")
        if (self.a ==0):
            if(self.b==0):
                string = '0'
            else:
                string = str(str(self.b)+"i")
        return string
    def __add__(self, rhs):
    # Method to add two complex numbers
        return Complex(self.a + rhs.a, self.b + rhs.b)
    def __mul__(self, rhs):
 # Method to multiply two complex numbers
        return Complex((self.a * rhs.a) - (self.b * rhs.b), (self.a * rhs.b) + (self.b * rhs.a))
    def __truediv__(self, rhs):
 # Method to divide two complex numbers
        return Complex((self.a * rhs.a + self.b * rhs.b) / (rhs.a ** 2 + rhs.b ** 2), (self.b * rhs.a - self.a * rhs.b) / (rhs.a ** 2 + rhs.b ** 2))

#t, a, b, c, d = [int(x) for x in input().split()]
#c1 = Complex(a,b)
#c2 = Complex(c,d)
""" if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2) """
""" a = Complex(3, 4)
b = Complex(5, 6)
c = Complex(3, 1)
d = Complex(2, 1)
print(str(a)) # equal to 3+4i
print(a + b) # equal to 8+10i
print(a * b) # equal to -9+38i
print(b * a) # equal to -9+38i
print(c / d) # equal to 1.4-0.2i """
""" a = Complex(2, 2)
print(a)
b = Complex(2, 0)
print(b)
c = Complex(2, -2)
print(c)
d = Complex(0, 2)
print(d)
e = Complex(0, 0)
print(e)
f = Complex(0, -2)
print(f)
g = Complex(-2, 2)
print(g)
h = Complex(-2, 0)
print(h)
i = Complex(-2, -2)
print(i) """