#include <stdio.h>

int greater_of(int x, int y){
    if (x>y){
        return x;
    }
    return y;
}

int main(){
    int a=3,b=17;
    printf("The greater of %d and %d is %d\n",a,b,greater_of(a,b));
    return 0;
}
