#include <stdio.h>
#include <math.h>
#define PI acos(-1.0)

int main(){

    float angle_in_degrees;
    int correct_inputs = 0;

    do {
        printf("Please enter an angle in degrees to convert to radians:\n");
        correct_inputs = scanf("%f",&angle_in_degrees);
        if (correct_inputs==0){
            printf("Invalid input\n");
        }
        fflush(stdin);
    }while (correct_inputs==0);
    
    printf("The angle in radians is %f\n",PI*angle_in_degrees/180.0);
    return 0;
} 
