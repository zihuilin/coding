#include <stdio.h>

int main(){

    long l = 123456789012345678;
    int size = sizeof(l);
    printf("l is %ld\n", l);
    printf("size of l is %d\n", size);
    return 0;
}
