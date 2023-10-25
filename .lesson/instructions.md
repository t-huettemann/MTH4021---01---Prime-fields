# Finite prime field arithmetic

## TASK 1

Use the variable G to define the finite field of order 257.

Use the variable z to find the element 1024 in G.

Define y to be the 2023rd power of z.

Define b to be the bolean variable which is

- ***true*** if the 256th power of z equals 1 in the field G,

- ***false*** otherwise.

Hint: Use the function ".is_one()".


## TASK 2

Write a function Order(x) that accepts a single argument x, which is supposed to be an element of a primefield, and returns a non-negative integer:

- Return value should be 0 if x is zero.

- Otherwise, return value is the smallest positive k such that the power x^k is one.

