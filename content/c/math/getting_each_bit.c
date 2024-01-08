#include <stdio.h>

int main(){
    int number = 8;
    for (int i=0;i<number;i++){
        printf("%d in binary: %d %d %d\n",i,i>>2&1,i>>1&1,i&1);
    }
    return 0;
}
