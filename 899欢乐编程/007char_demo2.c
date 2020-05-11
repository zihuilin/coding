#include <stdio.h>

int main(){
    char c;
    scanf("%c", &c);
    char c0 = '0';
    char c9 = '9';
    if (c >= c0 && c <= c9){
        printf("yes!\n");
    } else {
        printf("no!\n");
    }
        
    return 0;
}
