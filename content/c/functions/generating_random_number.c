#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int rand_int(int min, int max){
    int random_number = min+(rand()%(max-min+1));
    return random_number;
}

int main(){
    srand(time(NULL));
    for (int i=0;i<10;i++){
        printf("Our number is %d\n",rand_int(3,10));}
    return 0;
}
