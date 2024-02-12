# Getting Started with C
This is the start of the lessons on the C programming language. C is an imperative, compiled, statically-typed, portable language.

- *imperative*: we tell the computer how to accomplish a goal; we give it orders
- *compiled*: the computer translates the entire code into an executable/binary code which the machine can then understand
- *statically-typed*: we tell the computer exactly what type of data we want it to use instead of having it guess based on how we use the data; this makes our code run faster because time is not wasted on guessing
- *portable*: we write our code and use the compiler for whichever platform/device we want to run the code on; the compiler then translates it into the machine code for that device thus saving us from having to rewrite different versions of C for different machines; we simply use different compilers

## Boilerplate
Boilerplate is used to refer to the repetitive sections of code that developers have to type with little to no variation.

Examine the following C code snippet:

!{{./hello.c}}


#### Challenge
Answer the following questions:
- What would you consider to be C boilerplate?
- What is the **stdio.h** referring to?
- Is this header file necessary for every C program?
- What is the function *printf* used for?
- Why do we use the " symbol before and after *Hello world!*?

## Grammar in C
- **keywords** - these are **reserved** identifiers meaning that they cannot be used to mean anything else in your code than was intended by the language creator(s). Examples include **#include**, **int** and **return**
- **punctuations** - in the same way we use punctuations as boundaries or markers in the English language, we use them in C to demarcate sections of our code:
    - single-line comments begin with *//*
    - multi-line comments are surrounded by *\/\** and *\*\/*
    - functions are indicated by the name of the function followed by parentheses e.g. **main()** and **printf()**
    - *[* and *]* are used after arrays to indicate access to the individual elements in the array
    - commas are used to separate elements in a list and **semi-colons** are used to end statements in C.
- **comments** - these are ignored by the compiler; they are used to tell the reader the purpose of a section of code or to preserve unused code
- **literals** - these are items with constant/fixed values e.g. *0*,*1*,*-7*,*3E+23*,*"Hi"*
- **identifiers** - these are used to identify entities in the program. They can built-in or user-defined. Identifiers must be declared before they are used. This is because C programs are executed from top to bottom. There are various kinds of identifiers: 
    - data objects e.g. *i* and *age*
    - type aliases e.g. *size_t*
    - functions e.g. *main* and *printf*
    - constants e.g. *EXIT_SUCCESS*
    
- **functions** - these are named sections of code that can be reused
- **operators** - these are used to manipulate the state of a program. They can be used for initialization and assignment (=), comparison (==,<,<=,>,>=), increment (++), decrement (--), arithmetic (+,-,*,/)


