# Iterative Constructs Part 2
Here is some more information on how we use iterative constructs.

## Infinite loops
These are loops that have the potential to run forever.
!{{./infinite_loop.c}}

## Empty loops
These are loops that do no effective work in the program. They may happen by accident 
if we do not take care in how we write our code (usually by putting curly braces in
the wrong place).
!{{./empty_loop.c}}

## The goto directive
Looping behaviour can be achieved by the use of C's goto directive. We place a label
before a section of code and tell the computer to *go to* that section where the label is. 

### The Euclidean algorithm
The goto directive can be used to write a more readable form of the Euclidean algorithm:
!{{./goto_euclidean_algorithm.c}}

Notice that we do not declare any variables after the label. The algorithm is based on the fact that for an equation:
$$b=qa+r$$
the highest common factor (HCF) of **b** and **a** is the HCF of **a** and **r**
$$HCF(b,a)=HCF(a,r)$$
The algorithm is terminated when we get the HCF of **a** and *a remainder of **0***:
$$HCF(a,0)=\color{royalblue}a$$
This **a** is the HCF of the two numbers we started with.
