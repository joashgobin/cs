#include <stdio.h>
#include <time.h>

char* get_current_time(){
    time_t t;
    time(&t);
    return ctime(&t);
}

int main(){
    printf("The current time is %s\n",get_current_time());
    return 0;
}
