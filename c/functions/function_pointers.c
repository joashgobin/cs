/* Function pointers are used to point to code
 * whereas normal pointers point to data at a memory
 * location. We do not need to allocate and de-allocate
 * memory for function pointers as we do with normal pointers
 * A function's name is a way to get the function's address
 * Function pointers can be used to achieve the strategy pattern in C
 * a.k.a. dependency injection
 */

#include <stdio.h>

// using a typedef to make specifying function pointers easier
typedef int (*binary_operation_ptr)(int,int);

// defining a struct to act as a class with its own name and method
struct Strategy{
    char name[10];
    binary_operation_ptr operation;
    // OR int (*operation)(int,int); WITHOUT typedef
};

typedef struct Strategy Strategy;

int sum(int x,int y){
    return x+y;
}

int diff(int x,int y){
    return x-y;
}

void use_strategy(Strategy strategy){
    printf("The result of using %s wth 5 and 6 is %d\n",strategy.name,strategy.operation(5,6));
}

void do_calculation(int (*op)(int,int), int x, int y){
    printf("The result of the operation is %d\n",op(x,y));
}

int main(){
    // calls the sum function
    do_calculation(&sum,3,4);
    // does the same thing because the function name is sufficient to locate it
    do_calculation(sum,3,4);

    // create a strategy for addition
    Strategy addition;
    strcpy(addition.name,"Addition");
    addition.operation = sum;
    use_strategy(addition);

    // create a strategy for subtraction
    Strategy subtraction;
    strcpy(subtraction.name,"Subtraction");
    subtraction.operation = diff;
    use_strategy(subtraction);
    

    return 0;
}
