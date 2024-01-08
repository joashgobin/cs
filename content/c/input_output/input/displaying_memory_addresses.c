#include <stdio.h>

int main(){
    char character;
    printf("Please enter a character: ");
    scanf("%c",&character);
    printf("The character you entered (%c) is now located at %p\n",character,&character);
    return 0;
}
