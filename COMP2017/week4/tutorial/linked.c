#include <stdio.h>
#include <stdlib.h>

struct node {
    int value;
    struct node *next;
};

struct node *list_init(int value){
    struct node *new = calloc(1, sizeof(struct node));
    new->value = value;
    return new;
}

void list_add_before_head(struct node** head, int value){
    struct node *new = list_init(value);
    new->next=*head;
    *head = new;
}

int main(){
    struct node *list = list_init(5);

    list->next = 
    printf("%d\n", list->value);
    printf("%p\n", list->next);
}