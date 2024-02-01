# Arrays
Arrays are a way for us to store many values of a certain datatype under the same name.
Other languages have sets, lists and dictionaries which serve a similar purpose.
This saves us the time and energy of having to create unique names for each value we want to
store.

The format for defining an array is:
~~~c
type array_name[number_of_values];
~~~

## Integer arrays
We can *populate* an integer array by including the values in curly braces:
!{{./populating_an_integer_array.c}}

!{{./traversing_an_integer_array.c}}

## Strings (character arrays)
An array of characters is known as a **string**. We can declare a string using double quotations:
```c
char name[10] = "John Doe";
```
We do not need to specify the number of characters if we use the double quotations:

```c
char name[] = "John Doe";
```

We can traverse a string:
!{{./traversing_a_string.c}}
