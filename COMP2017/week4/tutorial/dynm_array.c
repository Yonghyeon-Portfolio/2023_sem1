#include <stdio.h>
#include <stdlib.h>

struct dyn_array{
    int capacity;
    int size;
    int *content;
};

struct dyn_array *dyn_array_init(int value){
    struct dyn_array *arr = malloc(sizeof(struct dyn_array));
    arr->capacity = 2;
    arr->size = 1;
    arr->content = malloc(arr->capacity * sizeof(int));
    arr->content[0] = value;
    return arr;
}

void dyn_add(struct dyn_array* dyn, int value){
    if (dyn->size >= dyn->capacity){
        dyn->capacity *= 2;
        // puts("capacity increased");
        dyn->content = realloc(dyn->content, dyn->capacity * sizeof(int));
        // puts("content memory increased");
    }
    dyn->content[dyn->size] = value;
    dyn->size += 1;
}

void print_dyn(struct dyn_array* dyn){
    for (int i = 0; i < dyn->size; i++){
        printf("%dth element: %d\n", i, dyn->content[i]);
    }
}

int main(){
    struct dyn_array *list = dyn_array_init(10);
    dyn_add(list, 1);
    dyn_add(list, 2);
    dyn_add(list, 3);
    dyn_add(list, 4);
    dyn_add(list, 5);
    dyn_add(list, 6);
    dyn_add(list, 7);
    dyn_add(list, 8);
    print_dyn(list);

}