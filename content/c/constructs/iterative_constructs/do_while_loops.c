#include <stdio.h>

int main(){
    int i = 0;

    do{
        printf("%d\n",i);
        i++;
    }while(i<10);
    
    int ret,number;
    do{
        printf("Please enter a valid number:\n");
        ret = scanf("%d",&number);

    }while(ret==0);
    printf("Ghee thanks!!");
}
