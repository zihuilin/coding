#include <stdio.h>

int main(){
    char c;
    scanf("%c", &c);

    if (c >= 'a' && c <'x')
        c = c + 3;
    else
        c = c - 23;

    printf("%c", c);

    return 0;
}
