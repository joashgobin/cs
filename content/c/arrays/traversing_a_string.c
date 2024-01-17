#include <stdio.h>
#include <string.h>

int main(){
    // there is no need to manually count the string size so we use []
    char word[] = "Hello there comrade";
    int count = 0;

    // traversing the string in the forward direction
    for (int i=0;i<strlen(word);i++){
        
        // printing the current letter
        printf("The letter at index %d is %c\n",i,word[i]);
        
        // incrementing count if the current letter is an 'a'
        if (word[i]=='a'){
            count++;
        }
    }
    printf("We found %d a's in \"%s\"\n",count,word);

    // traversing the string in reverse
    printf("The reversed word is ");
    for (int i=strlen(word)-1;i>=0;i--){
        printf("%c",word[i]);
    }

}
