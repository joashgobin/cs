/*
This program simulates a coin toss done with 100 coins
Coins are drawn after each throw and the numbers of heads and tails
are counted and displayed
The tossing function is repeated and the drawing function is called recursively until no heads remain
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <string.h>

void draw_coins();
void toss_coins();

char coins[100];
int throw_count;

//function to keep the program busy for a fraction of a second
void tiny_pause(){
    int sum = 0;
    for (int i=0;i<=100000000;i++){
        sum+=i;
    }
}

//function to set the initial conditions of the experiment: all heads and zero throws
void reset_coins(){
    throw_count = 0;
    for (int i=0;i<100;i++){
        coins[i] = 'o';
    }
    system("cls");
}

//function to display coins and count the numbers of heads and tails
void draw_coins(){
    int heads=0,tails=0;
    printf("Checking coins after %d throws:\n",throw_count);
    for (int i=0;i<100;i++){
        printf("%c",coins[i]);
        if (i%50==49){
            printf("\n");
        }
        if (coins[i]=='o'){
            heads+=1;
        }
        else{
            tails+=1;
        }
    }
    printf("Heads(o): %d, Tails(-): %d\n\n\n",heads,tails);
    tiny_pause();
    if (heads>0){
        toss_coins();
        draw_coins();
    }
}

//function to randomly flip the heads which are present in the set of coins
void toss_coins(){
    for (int i=0;i<100;i++){
        if (coins[i]=='o'){
            if (rand()%100<50){
                coins[i] = '-';
            }
        }
    }
    throw_count+=1;
}

int main(){
    reset_coins();

    // setting the seed of the random number generator to the current time so that results of the rand() function will always vary
    srand(time(0));
    draw_coins();

    return 0;
}

