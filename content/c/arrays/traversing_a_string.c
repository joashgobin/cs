#include <stdio.h>
#include <string.h>

int main(){
    char word[] = "Hello there comrade";
    int count = 0;

    for (int i=0;i<strlen(word);i++){
        printf("The letter at index %d is %c\n",i,word[i]);
        if (word[i]=='a'){
            count++;
        }
    }
    printf("We found %d a's in \"%s\"\n",count,word);

    printf("The reversed word is ");
    for (int i=strlen(word)-1;i>=0;i--){
        printf("%c",word[i]);
    }

}
