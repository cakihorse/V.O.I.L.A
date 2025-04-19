/******************************************************************************

    write the a function that, beginning whit a, displays the lowercase
    in ascending order, on a single line. It must be prototyped as 
    follows: int my_print_alpha(void);

*******************************************************************************/

#include <stdio.h>

int my_print_alpha();

int main()
{
    my_print_alpha();
    return 0;
}

int my_print_alpha()
{
    //Return abcdefghijklmnopqrstuvwxyz in one single line.
    //and then return the inverse of the alphabet.
    //a = 97 / z = 122
    char first_letter;
    first_letter = 122;
    while (first_letter >= 97)
    {
        putchar(first_letter);
        first_letter--;
    }
    return 0;
}
//need to do a my_putchar() ?

