#include <stdio.h>

struct Person{
    char name[50];
    int age;
};

typedef struct Person person_t;

int main(){
    struct Person p = {"Isaac", 21};
    person_t p2 = {"John", 23};
    printf("%s %d\n", p.name, p.age);
    printf("%s %d\n", p2.name, p2.age);
    return 1;
}