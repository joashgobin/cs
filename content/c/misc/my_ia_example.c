/*Teacher management system
 *
 * Functional requirements:
 * - store teacher information
 * - read teacher information
 * - add teacher information
 * - calculate net salary from gross salary
 *
 * Non-functional requirements (acceptance criteria):
 * - Error handling for incorrect inputs
 * - Messages to notify when a mistake is made
 *
 */

#include <stdio.h>

struct Teacher{
    char fname[100];
    char lname[100];
    int age;
    double height;
    float gross_salary;
};

typedef struct Teacher Teacher;

// function prototypes
void get_all_teachers_from_database();
void add_teacher_to_database(Teacher);
float calculate_net_salary(float);
void add_teacher(void);

void clear_input_buffer(){
    int ch;
    while((ch=getchar())!='\n'&&ch!=EOF);
}

float calculate_net_salary(float gross_salary){
    float tax_rate = 0.3;
    return gross_salary*(1.0-tax_rate);
}

void get_all_teachers_from_database(){
    Teacher current_teacher;
    FILE* fp = fopen("my_file.txt","r");
    while(fscanf(fp,"%s %s %d %lf %f",current_teacher.fname,current_teacher.lname,&current_teacher.age,&current_teacher.height,&current_teacher.gross_salary)!=EOF){
        printf("Found teacher '%s %s'  with age: %d years, height: %g cm, gross salary: $%.2f\n",current_teacher.fname,current_teacher.lname,current_teacher.age,current_teacher.height,current_teacher.gross_salary);
        printf("Their net salary is %.2f\n\n",calculate_net_salary(current_teacher.gross_salary));
    }
    fclose(fp);
}

void add_teacher_to_database(Teacher teacher){
    FILE* fp = fopen("my_file.txt","a");
    fprintf(fp,"%s %s %d %g %f\n",teacher.fname,teacher.lname,teacher.age,teacher.height,teacher.gross_salary);
    fclose(fp);
}

void add_teacher(void){
    Teacher new_teacher;
    int correct_values;
    printf("Input the teacher's name:\n");
    scanf("%s %s",new_teacher.fname,new_teacher.lname);
    accept_age:
    printf("Input the teacher's age in years:\n");
    correct_values = scanf("%d",&new_teacher.age);
    if (correct_values!=1){
        printf("That is not an integer!\n");
        clear_input_buffer();
        goto accept_age;
    }
    accept_height:
    printf("Input the teacher's height in cm:\n");
    correct_values = scanf("%lf",&new_teacher.height);
    if (correct_values!=1){
        printf("That is not a real number!\n");
        clear_input_buffer();
        goto accept_height;
    }
    accept_salary:
    printf("Input the teacher's gross salary:\n");
    correct_values = scanf("%f",&new_teacher.gross_salary);
    if (correct_values!=1){
        printf("That is not a real number!\n");
        clear_input_buffer();
        goto accept_salary;
    }

    printf("Adding teacher '%s %s', age: %d years, height: %g cm, gross salary: $%.2f\n",new_teacher.fname,new_teacher.lname,new_teacher.age,new_teacher.height,new_teacher.gross_salary);
    add_teacher_to_database(new_teacher);
}

void menu(){
    int choice;
    printf("Please choose an option:\n");
    printf("1 - Add a teacher\n");
    printf("2 - See all teachers\n");
    scanf("%d",&choice);

    clear_input_buffer();

    switch(choice){
        case 1:
            add_teacher();
            break;
        case 2:
            get_all_teachers_from_database();
            break;
        default:
            printf("Invalid choice\n");
    }
}

int main(void){
    while(1){
        menu();
    }
    return 0;
}
