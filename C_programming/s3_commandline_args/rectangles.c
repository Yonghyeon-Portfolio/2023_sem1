#include <stdio.h>
#include <stdlib.h> 

int main(int argc, char *argv[]){
    if (argc != 3){
        puts("Two command line arguments need to be provided for this program");
        puts("Two argumnets each represent the width and height of a rectangle");
        return 1;
    }
    char *width = argv[1];
    char *height = argv[2];

    // Pointer may be passed onth the second argument of the function strtod
    // for error handling. (if conversion fails, pointer points to the first
        // character that caused the error)
    double width_dob = strtod(width, NULL);
    double height_dob = strtod(height, NULL);

    if (width_dob <= 0 || height_dob <= 0){
        puts("The width or the height of the rectangle provided is invalid");
        return 1;
    }
    printf("The width of the rectangle: %2.3f\n", width_dob);
    printf("The height of the rectangle: %2.3f\n", height_dob);

    double area = width_dob * height_dob;
    double perimeter = 2 * (width_dob + height_dob);

    printf("Area: %2.3f\n", area);
    printf("Perimeter: %2.3f\n", perimeter);

    return 0;
}