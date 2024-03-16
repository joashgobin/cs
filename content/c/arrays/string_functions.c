#include <stdio.h>

int main(){
    char first_name[] = "John";
    char last_name[] = "Doe";
    char buffer[100];

    printf("Before concatenation:\n");
    printf("The first name is %s\n",first_name);
    printf("The last name is %s\n",last_name);

    printf("0 The buffer is currently: %s\n",buffer);


    // strcat(destination, source);
    strcat(buffer,first_name);
    printf("1 The buffer is currently: '%s'\n",buffer);


    strcat(buffer," ");
    printf("2 The buffer is currently: '%s'\n",buffer);

    strcat(buffer,last_name);
    printf("3 The buffer is currently: '%s'\n",buffer);

    char buffer_2[100] = "Hello there";
    printf("4 Buffer 2 is currently: '%s'\n",buffer_2);

    strcpy(buffer_2,buffer);
    printf("5 Buffer 2 is currently: '%s'\n",buffer_2);

    char name[] = "Mary Sue";

    printf("Forward:\n");
    for (int i=0;i<strlen(name);i++){
        printf("The character at index %d is %c\n",i,name[i]);
    }

    printf("Reverse:\n");
    for (int i=strlen(name)-1;i>=0;i--){
        printf("The character at index %d is %c\n",i,name[i]);
    }

    return 0;
}
