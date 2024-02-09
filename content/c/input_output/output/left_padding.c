#include <stdio.h>

int main(){
    int id = 9;
    char padded_text[10];
    sprintf(padded_text,"%08d\n",id);
    printf("The student's ID is %s\n",padded_text);
    return 0;
}
