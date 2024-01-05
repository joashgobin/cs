# Functions
These are reusable sections of code. They can be built-in or user-defined. Functions
allow us to write code that can be modified in one place and change the effect in 
multiple sections. Functions are also sometimes referred to as routines because of 
how we use them to group a set of related steps under a single name. A function in C
follows the format:

```c
return_type function_name(argument_1,argument_2,...){
    do_something;
    do_something_else;
    return return_value;
}
```
Here is an example of a function being used to draw a line:

!{{./print_line.c}}

We *call* the function **print_line()** from the main() function. We pass the control
from the main() function to the print_line() function and when it is finished executing it
passes control back to the main() function.

#### Challenge
- Change the *'s used to draw the line in print_line() into 0's
- In how many places does the output of the program change?
- Write a function count_to_ten() which counts from 1 to 10 every time it is called and call it 
from the main() function

## Functions with arguments but no return values
A parameter is a variable which stores a value being passed into a function. When we give 
a parameter a value, we refer to this value as an argument. Arguments are the *inputs* of
a function. A function may have any number of arguments even no arguments.

!{{./count_to.c}}

The function count_to() *accepts* one **integer** argument and runs a for loop to count from 1 to
that number. Notice that we did not have to create a variable within the function
count_to() in order for the program to work. By putting *int number* in the parentheses of the function definition
we are declaring a **local automatic variable** called *number*.

A *local automatic variable* can only be accessed within the function's body and is
created without us having to put it in the function's body (automatic).

### Declarative programming
C is a procedural language which means that we specify the steps (the procedure) that the computer
must take in order to achieve the desired outcome. When we engage in declarative programming,
we tell the computer **what to do** rather than *how to do it*.

Functions are one way in which we can achieve this declarative style of coding. It is 
much easier to run **count_to(1500)** than it is to type out the steps required to
do the counting. Thus by using the *interface* **count_to(number)**, we tell the computer what to do without
telling it how to do it. 

Of course, someone would have had to write the *implementation*
of the function in the first place and that someone might even be you. The interesting idea
is that this implementation can be done using a for loop or a while loop or a goto directive.
Regardless of the way we do the implementation, the code **count_to(1500)** will
always do exactly that - *count to 1500*.

Our coding style should move towards being **declarative** (telling the computer what to do)
instead of always being *imperative* (telling the computer how to do it). The current *n*
lines of code should make the next *n* lines of code easier to write.

##### printf()
Unless you've read the implementation of printf() from the source code of your C compiler,
you won't know what the printf() function does in order to output text to the terminal.
That's the amazing thing about declarative programming. We focus on what should be achieved rather than
telling the machine how to achieve it.

[Read more in Functions part 2](./functions_part_2.md)
