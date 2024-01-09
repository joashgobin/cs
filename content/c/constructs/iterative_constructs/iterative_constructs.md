# Iterative Constructs
When we are solving a problem, we may want to repeat a section (block) of our code.
This is achieved through the use of *iterative constructs*. In C, we have three (3)
common iterative constructs:
- for loops
- while loops
- do-while loops

Iterative constructs can be bounded (e.g. **for loops**) or unbounded (**while** and **do-while loops**).

## For loops
The **for loop** is a bounded loop. This is because we can tell how many times it will
be executed before termination. We can know the number of iterations from how we construct the for loop.
!{{./for_loops.c}}

## While loops
The **while loop** is a type of unbounded iteration. This is because its execution is not 
terminated when a certain number of iterations are finished but rather when a condition is met.
This means that a while loop and run 10 or 1000 or an infinite number of times based on if the condition is met.

The while loop checks the condition *before executing the block of code*. This means
that it is possible for the contents of a while loop to never be executed.
!{{./while_loops.c}}

#### Challenge
- Write a program to print the multiples of 3 from 0 to 30
- Write a program to print the factors of 21
- Write a program to print the numbers 0 to 20 excluding 3 and 7
- Write a program which will count from 1 to a number input by the user only if that
number is positive

## Do-while loops
A do-while loop will *always run at least once* because the condition is checked at
the end of each iteration.
!{{./do_while_loops.c}}

#### Challenge
- Write a program that repeats until the user enters the correct password
- Write a program that asks the user to say true or false to an inequality of the form **a>b**
where **a** and **b** are randomly generated. The program ends when the user gives the wrong truth value
- Write a program to find all of the factors of a natural number input by the user

[The lesson on loops continues here](./iterative_constructs_part_2.md)
