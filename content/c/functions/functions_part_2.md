# Functions Part 2
We continue by learning about functions with return values and those with both return values and 
arguments.

## Functions with return values but no arguments
Here is a function that is used to get the current time:
!{{./current_time.c}}

The function doesn't accept any values but it does return a string.
*char** is just a way to indicate that the function returns a string. The current time
is the string being returned.

## Functions with both arguments and return values
When we do functions in algebra we have an input (x) and a return value (y). This can
be achieved in C:
!{{./f_of_x.c}}

The return value of a function takes the place of the function when the function passes 
the execution back to the main() function (or whichever function called it). Thus in this 
example, the code *f(x)* is replaced by the value of f(x) and this is stored as y in the loop;
