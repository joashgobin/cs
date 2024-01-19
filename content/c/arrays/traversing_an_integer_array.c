#include <stdio.h>
#include <math.h>

int main(){
    int numbers[90];
    

    for (int i=0;i<90;i++){
        numbers[i] = pow(i+1,3);
    }

    for (int i=0;i<30;i++){
        printf("The number at index %d is %d\n",i,numbers[i]);
    }

    return 0;
}
