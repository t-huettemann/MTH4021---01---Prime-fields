import sys
sys.path.insert(0, '.lesson/')

import rings_and_fields as r

# creating a prime field object F
F = r.primefield(7)
# show output when object is printed
print("F=", F)

# define an element of F
t = F(38)
print("t=", t)

# check if t is zero
print("t=0?", t.is_zero())

# check if t is one
print("t=1?", t.is_one()

# compute t^3
print("t^3=", t.power(3))

# Exercises

G = r.primefield(257)
z = G(1024)
y = z.power(2023)
b = z.power(256).is_one()

print(G, z, y, b)
