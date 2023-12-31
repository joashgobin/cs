#include <stdio.h>

// not p
int not(int p){
    return !p;
}

// p or q
int or(int p,int q){
    return p||q;
}

// p and q
int and(int p,int q){
    return p&&q;
}

// p implies q
int implies(int p,int q){
    return !p||q;
}

int main(){
    printf("p\tq\tnot p\tnot q\tp or q\tp and q\tp->q\tp->~q");
    printf("\n----------------------------------------------------------------\n");
    for (int n=0;n<4;n++){
        int p = (n>>1)&1;
        int q = n&1;
        printf("%d\t%d\t",p,q);
        printf("%d\t",not(p));
        printf("%d\t",not(q));
        printf("%d\t",or(p,q));
        printf("%d\t",and(p,q));
        printf("%d\t",implies(p,q));
        printf("%d",implies(p,not(q)));
        printf("\n");
    }
    return 0;
}
