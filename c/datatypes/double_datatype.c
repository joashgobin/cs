/* Doubles are 8 bytes (64 bits) whereas float are only 4 bytes
 * 11 bits for the exponent, 1 bit for the sign
 * and 52 bits for the manstissa
 * This datatype ranges from 1.7E-308 to 1.7E+308
 * The format specifier is %g
 */

#include <stdio.h>
#include <math.h>
#define PI acos(-1.0)

int main(){
    double length = 0.7;
    double period = 2*PI*sqrt(length/9.81); 
    
    printf("The period of a simple pendulum with length %g m is %g s",length,period);
}
