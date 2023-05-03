#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define INIT_CAPACITY (5)
#define GROW_FACTOR (2)

struct shopper{
    char name[50 + 1];
    char item[50 + 1];
    unsigned int age;
};

struct shopper_array{
    int capacity;   
    int size;
    struct shopper *list;
};

typedef struct shopper_array s_arr;

s_arr init_shopper_array(){
    s_arr shoppers = {INIT_CAPACITY, 0, NULL};
    shoppers.list = malloc(sizeof(struct shopper) * INIT_CAPACITY);
    if (shoppers.list == NULL){
        puts("Lacking memory space. Exiting the program..");
        exit(1);
    }
    return shoppers;
}

int add_shopper(s_arr *shoppers, struct shopper *shopper){
    if (shoppers->size == shoppers->capacity){
        shoppers->capacity *= GROW_FACTOR;
        shoppers->list = realloc(shoppers->list, shoppers->capacity * sizeof(struct shopper));
        
        if (shoppers->list == NULL){
            puts("Lacking memory space. Exiting the program..");
            exit(1);
        }   
    }
    shoppers->list[shoppers->size] = *shopper;
    shoppers->size += 1;

    return 1;
}

int main(){
    puts("Welcome to ShopaMocha,");
    
    s_arr shoppers = init_shopper_array();

    while (1){
        struct shopper info;
        if (scanf("%s %u %s", info.name, &(info.age), info.item) != 3)
            break;
        add_shopper(&shoppers, &info);
    }

    for (int i = 0; i < shoppers.size; i++){
        struct shopper s = shoppers.list[i];
        printf("Customer %2d, Name: %s, Age: %u, Looking for: %s\n", 
            i, s.name, s.age, s.item);
    }

    return 1;
}
