#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "algo_util.h"

void init_rand_ints(int arr[], int len) {
    srand(time(NULL));
    for (int i=0; i<len; i++) {
        arr[i] = rand();
    }
}
/*
int main(){
    int a[100];
    init_rand_ints(a, 100);
    for (int i=0; i<100; i++) {
        printf("%d\n", a[i]);
    }

}
*/
