#include <stdio.h>
#include <math.h>

int main(){
    double numbers[90];
    for (int i=0;i<90;i++){

        // casting i+1 as a double and converting the angle to radians
        numbers[i] = sin(M_PI/180.0*(double)(i+1));
        printf("The angle at index %d is sin(%d)=%g\n",i,i+1,numbers[i]);

    }
    return 0; 
}
