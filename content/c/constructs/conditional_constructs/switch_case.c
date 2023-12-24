#include <stdio.h>

int main(){
    char grade;
    printf("Please enter your grade: ");
    scanf("%c",&grade);

    switch(grade){
        case 'A':
            printf("You did great work\n");
            break;
        case 'B':
            printf("You did good work\n");
            break;
        case 'C':
            printf("You can do better\n");
            break;
        default:
            printf("You need to work harder\n");
    }
}
