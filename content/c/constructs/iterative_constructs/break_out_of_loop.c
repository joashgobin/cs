#include <stdio.h>

int main(){
    int i=0;
    while (i<=10){
        printf("i is %d\n",i);
        // exit loop if i is 7
        if (i==7){
            break;
        }
        i++;
    }
    printf("The loop has finished\n");
    return 0;
}
