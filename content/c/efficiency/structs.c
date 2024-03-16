#include <stdio.h>
typedef int integer;

struct Person{
    char name[100];
    integer age;
    float height;
    char job[100];
};

typedef struct Person Person;
typedef struct Person Student;
typedef struct Person Teacher;

void tell_me_about(Person person){
    printf("This is %s\n",person.name);
    printf("Their age is %d\n",person.age);
    printf("They are %f in height\n",person.height);
    printf("They are a %s\n",person.job);
}

int main(){
    Student student_1;
    Student pupils[30];

    char my_string[] = "Hello";

    strcpy(student_1.name,"Sara");
    student_1.age = 13;
    student_1.height = 180;
    strcpy(student_1.job,"Cat owner");


    Teacher principal;
    strcpy(principal.name,"Ms. Lall");
    principal.age = 43;
    principal.height = 220;
    strcpy(principal.job,"Principal");


    tell_me_about(student_1);
    tell_me_about(principal);

    return 0;
}
