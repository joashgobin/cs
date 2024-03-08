#include <stdio.h>

int main(){
    char name[] = "John Doe";
    int age = 13;
    FILE* fp = fopen("my_file.txt","w");
    fprintf(fp,"Hello how are you?\n");
    fprintf(fp,"My name is %s\n",name);
    fprintf(fp,"I am %d years old\n",age);
    fclose(fp);
    return 0;
}
