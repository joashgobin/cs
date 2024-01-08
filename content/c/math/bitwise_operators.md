# Bitwise Operators
There are six (6) bitwise operators in C:
- Bitwise NOT/complement (**~**)
- Bitwise AND (**&**)
- Bitwise OR (**|**)
- Bitwise XOR (**^**)
- Left shift (**<<**) 
- Right shift (**>>**)

## Bit shifting
We can use the *<<* and *>>* operators to *bit shift* a number. Left shifting a number by 1 digit is the same
as multiplying the number by two. Right shifting the number by 1 digit is the same as an integer division by 2
(dividing by 2 and round the result downwards).

We can use the right shift and a logical AND to access each bit in a number:
!{{./getting_each_bit.c}}

Doing a logical AND with a number gives us the rightmost bit.
