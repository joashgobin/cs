#include <stdio.h>

double f(int x){
    double y = x*x+5*x+6;
    return y;
}

int main(){
    for (int x=0;x<10;x++){
        double y = f(x);
        printf("(%d,%g)\n",x,y);
    }
    return 0;
}
