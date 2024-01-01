#include <stdio.h>

// checking feature extracted out as function
void even_or_odd(int x){
    if (x%2==0){
        printf("%d is even\n",x);
    }else{
        printf("%d is even\n",x);
    }
}

int main(){

    // no extraction
    for (int x=0;x<10;x++){
        if (x%2==0){
            printf("%d is even\n",x);
        }else{
            printf("%d is even\n",x);
        }
    }

    // with extraction
    for (int x=0;x<10;x++){
        even_or_odd(x);
    }
    return 0;
}
