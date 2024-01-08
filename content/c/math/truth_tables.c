#include <stdio.h>

int not(int p){
    return !p;
}

int or(int p,int q){
    return p||q;
}

int and(int p,int q){
    return p&&q;
}

int implies(int p,int q){
    return !p||q;
}

int main(){
    printf("p\tq\tnot p\tp or q\tp and q\tp->q");
    printf("\n-------------------------------------------------\n");
    for (int n=0;n<4;n++){
        int p = n/2;
        int q = n%2;
        printf("%d\t%d\t",p,q);
        printf("%d\t",not(p));
        printf("%d\t",or(p,q));
        printf("%d\t",and(p,q));
        printf("%d",implies(p,q));
        printf("\n");
    }
    return 0;
}
