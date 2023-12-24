#include <stdio.h>

int main()
{
    // write a while loop to print the numbers 0 to 5
    int i = 0;
    while(i<=5){
        printf("The value of i is %d\n",i);
        i = i+1; // OR i+=1 OR i++
    }

    // write a while loop to print the first 10 multiples of 3
    int n = 0;
    while(n<=10){
        printf("%d x %d = %d\n",n,3,n*3);
        n+=1;
    }

    // write a loop which will run until a PIN 1234 is entered
    int pin;
    while(1){
        // ask for user input and use break when the PIN is correct
        printf("Please enter your pin:\n");
        scanf("%d",&pin);
        if (pin==1234){
            printf("Correct pin!! You get a cookie...");
            break;
        }else{
            printf("Wrong pin bro...\n");
        }
    }
    return 0;
}
