#include <stdio.h>

int main(){
    int original_a=14,original_b=12344;
    int a=original_a,b=original_b,quot,rem;
    
    // declaring label called 'start'
    start:
    quot = b/a;
    rem = b%a;
    printf("%d = %d x %d + %d\n",b,quot,a,rem);
    
    if (rem==0){
        printf("The HCF of %d and %d is %d\n",original_a,original_b,a);
    }
    else{
        b = a;
        a = rem;
        // jumping back to the 'start' label
        goto start;
    }
    return 0;
}
