#include <stdio.h>

int main()
{
    int i = 0;
    while(i<=5){
        printf("The value of i is %d\n",i);
        i = i+1; // OR i+=1 OR i++
    }

    int pin;
    while(1){
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
