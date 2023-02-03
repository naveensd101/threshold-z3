from z3 import *

#from z3 import *
#s = Optimize()
#x = Int('x')
#y = Int('y')
#z = Int('z')
#a = Bool('a')
#b = Bool('b')
#c = Bool('c')
#c = Bool('d')
#a = (x+y+z == 1)
#b = (x+y+z == 2)
#c = (x+y+z == 3)
#d = (x+y+z == 4)
##our threshold k
#k=2
#s.add(z3.PbGe([(a,1),(b,1),(c,1),(d,1)], k))
#print(s.check())
#print(s.model())


x0 = Real('x0')
x1 = Real('x1')
x2 = Real('x2')
x3 = Real('x3')

b0 = Bool('b0')
b1 = Bool('b1')
b2 = Bool('b2')
b3 = Bool('b3')
b4 = Bool('b4')
b5 = Bool('b5')
b6 = Bool('b6')
b7 = Bool('b7')


s = Optimize()
b0 = (6*x0+10*x1+11*x2+3*x3==17)
b1 = (10*x0+1*x1+8*x2+7*x3==8)
b2 = (4*x0+3*x1+14*x2+2*x3==17)
b3 = (15*x0+2*x1+11*x2+2*x3==0)
b4 = (5*x0+15*x1+10*x2+3*x3==0)
b5 = (14*x0+5*x1+17*x2+9*x3==0)
b6 = (17*x0+5*x1+13*x2+14*x3==0)
b7 = (16*x0+2*x1+5*x2+17*x3==0)

s.add_soft(b0)
s.add_soft(b1)
s.add_soft(b2)
s.add_soft(b3)
s.add_soft(b4)
s.add_soft(b5)
s.add_soft(b6)
s.add_soft(b7)

print(s.check())
print(s.model())

m = s.model()
c0 = m.evaluate(b0)
c1 = m.evaluate(b1)
c2 = m.evaluate(b2)
c3 = m.evaluate(b3)
c4 = m.evaluate(b4)
c5 = m.evaluate(b5)
c6 = m.evaluate(b6)
c7 = m.evaluate(b7)

print(f'c0 =  {c0}')
print(f'c1 =  {c1}')
print(f'c2 =  {c2}')
print(f'c3 =  {c3}')
print(f'c4 =  {c4}')
print(f'c5 =  {c5}')
print(f'c6 =  {c6}')
print(f'c7 =  {c7}')
