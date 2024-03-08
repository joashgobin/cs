# File Operations
!mc{{
Why do you think we need to be able to access files in C?
To store data after the program has been executed
To make our code look fancy when people try to read it
To flex on our friends
To repeat a section of code for a specific number of times
}}

## File pointer
In C, we need to create a pointer to the file we want to interact with. The **fopen()** helps us
to create this file pointer. It accepts two arguments -
the path to the file we want to use and the *access mode*. There are many access modes, the most common being write, read and append.

We need to use the **fclose()** function in order to close the file.

```c
FILE* fp = fopen("my_file.txt",w);// or r or a
// write to or read from the file
fclose(fp);
```

## Writing to a file
We can use **fprintf()** in order to add text to a file in the same way that we add text to the console using
*printf()*:

!{{./writing_to_a_file.c}}

For the write mode, there is no need to create the file if it does not already exist. It should be noted that if the file already exists, then the contents of that file will be erased when we open it in write mode.

!mc{{
Is the file automatically created when using fopen() in write mode?
Yes
No
}}

## Reading from a file
We use the **fscanf()** function to read the contents of a file. We instruct the computer to read using a while loop, with the end condition being when the end of the file is encountered.

!{{./reading_from_a_file.c}}

!mc{{
Why do the printed lines not match the lines of the file but instead appear to be word by word?
The format specifier %s is for every character up to the space character
The format specifier %s is for every character up to the newline character
The format specifier %s is for every character up to the curly braces
}}
