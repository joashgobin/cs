#include <stdio.h>

int main(){
    int age;
    printf("Please enter your age: ");
    scanf("%d",&age);

    // no inversion
    if (age>=18){
        printf("You are an adult\n");
        if (age>=65){
            printf("You are also a senior citizen\n");
        }
    }
    else{
        printf("You are not an adult\n");
    }
    
    // with inversion
    if (age>=65){
        printf("You are an adult\n");
        printf("You are also a senior citizen\n");
        return 0;
    }
    if (age>=18){
        printf("You are an adult\n");
        return 0;
    }
    
    printf("You are not an adult\n");

    return 0;
}
