# Functions as Modules
In C, we use functions as the basic unit of modular design. Modular design is the practice of designing a system in *modules*. A module is any entity with an *interface* and an **implementation**. The interface provides an abstraction (a simplified view of an entity which omits unimportant details) of the module.

>An interface is a contract/intersection between the system and the environment.
Credits: [Robert Elder](https://blog.robertelder.org)

Functions act as modules in C. The definition of the function determines the interface. Take for example the following:

!{{./count_to.c}}

By just typing **count_to(number)**, we can use the function. This is the interface. The implementation is the actual body of the function. Appreciate how we do not need to know what the body of the function looks like in order to use it. We only need to know that we must pass an integer into the function.

We can use a simple diagram to represent this module:

!module{{count_to(number);implementation;width=50}}
