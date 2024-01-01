#include <stdio.h>

double f(int input){
    double output = input*input;
    return output;
}

int main(){
    for (int x=0;x<10;x++){
        double y = f(x);
        printf("(%d,%g)\n",x,y);
    }
    return 0;
}
