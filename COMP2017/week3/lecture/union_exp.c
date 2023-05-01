#include <stdio.h>

enum catalog_type {book, film};

struct catalog{
    char *title;
    enum catalog_type type;

    union creator{
        struct book{
            char *author;
            char *ISBN;
        } book_info;
        
        struct film{
            char *director;
            char *producer;
        } film_info;
    } info;
};

int main(){
    union creator hp_info ={.book_info = (struct book){"J.K. Rowling", "Scholatic"}};
    struct catalog C = {"Harry Potter", book, .info = hp_info};

    printf("title: %s \nauthor: %s \nisbn: %s\n", 
        C.title, C.info.book_info.author, C.info.book_info.ISBN);
}