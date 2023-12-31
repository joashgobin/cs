/* typedef can be used to create an alias for another
 * datatype. We can use it to give more meaning to our
 * variable declarations without changing the underlying
 * functionality achieved
 * typedef helps us with readability and maintainability
 */

#include <stdio.h>
#include <string.h>

typedef int phone_number;
typedef int integer;
typedef char string[100];

struct Vector2{
        double x;
        double y;
};

typedef struct Vector2 Vector2;

struct Person{
    string name;
    integer age;
    phone_number contact_number;
    Vector2 position;
};

typedef struct Person Person;

int main(){
    Person person; 
    strcpy(person.name,"John James");
    person.age = 23;
    person.contact_number = 1234567;
    person.position.x = 0;
    person.position.y = 2;
    printf("The person's name is %s\n",person.name);
    printf("Their age is %d\n",person.age);
    printf("Their phone number is %d\n",person.contact_number);
    printf("Their current position is (%g, %g)\n",person.position.x,person.position.y);
    return 0;
}
