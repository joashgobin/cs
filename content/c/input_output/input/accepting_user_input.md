# Accepting User Input
In C, we can use the function scanf()* to accept values from the user.
There are other functions, some of which we will address later on.

The basic format for using scanf() is:
```c
scanf(format_string,address_1,address_2,...);
```

Take for example asking the user for their age:
!{{./asking_for_age.c}}

## The ampersand, &
We use the **ampersand (&)** to specify that we want to use the **address (memory location)** of the variable that follows.
In this case, the variable is age. *Scanf()* requires the address of the variable in order to change its value.
This is unlike printf() which takes a copy of the variable (no ampersand is needed in order to get a copy).

## Printing the memory address of a variable
It is good to know the placeholder/format specifier to print memory addresses in C:
!{{./displaying_memory_addresses.c}}
