#include <stdio.h>

void count_to(int number){
    printf("Let's count from 1 to %d\n",number);
    for (int i=1;i<=number;i++){
        printf("%d\n",i);
    }
}

int main(){
    count_to(5);
    count_to(10);
    return 0;
}
