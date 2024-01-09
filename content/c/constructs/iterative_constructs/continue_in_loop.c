#include <stdio.h>

int main(){
    for (int i=0;i<=10;i++){
        printf("%d\n",i);
        if (i%2==0){
            continue;
        }
        // not executed if the number is even
        printf("%d is odd\n",i);
    }
    printf("The loop has finished\n");
    return 0;
}
