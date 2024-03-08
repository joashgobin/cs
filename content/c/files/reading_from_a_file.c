#include <stdio.h>

int main(){
    // string variable to store temporary data
    char buffer[100];
    FILE* fp = fopen("my_file.txt","r");
    // loop through the contents until the end of the file is found
    while(fscanf(fp,"%s",buffer)!=EOF){
        // for every iteration, buffer is used to store the string detected
        printf("%s\n",buffer);
    }
    return 0;
}
