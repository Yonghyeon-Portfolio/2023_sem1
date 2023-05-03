#include <stdio.h>
#include <string.h>
#include <stdlib.h>

struct person{
    char name[32];
    int age;
};

int compare_age(void *a, void *b){
    const struct person *p1 = a;
    const struct person *p2 = b;
    return p1->age - p2->age;
}

int compare_name(void *a, void *b){
    const struct person *p1 = a;
    const struct person *p2 = b;
    return strcmp(p1->name, p2->name);
}

void bubble_sort(void *elements, size_t elem_n, size_t size, int (*cmp)(void*, void*)){
    void *tmp = malloc(size);
    for (int i = 0; i < elem_n-1; i++){
        for (int j = 0; j < elem_n-1-i; j++){
            void *e1 = elements + size * j;
            void *e2 = e1 + size;
            if (cmp(e1, e2) > 0){
                memcpy(tmp, e1, size);
                memcpy(e1, e2, size);
                memcpy(e2, tmp, size);
            }
        }
    }
    free(tmp);
}

int main(){
    struct person ppl[4] = {
        {"Issac Kim", 21},
        {"John Kim", 23},
        {"Alian Rose", 35},
        {"Bobby Roid", 19}
    };

    bubble_sort(ppl, 4, sizeof(struct person), compare_age);
    for (int i = 0; i < 4; i++)
        printf("name: %s, age: %d\n", ppl[i].name, ppl[i].age);

    putchar('\n');

    bubble_sort(ppl, 4, sizeof(struct person), compare_name);
    for (int i = 0; i < 4; i++)
        printf("name: %s, age: %d\n", ppl[i].name, ppl[i].age);
}