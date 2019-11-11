#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include "algo_util.h"

void init_rand_ints(int arr[], int len) {
    srand(time(NULL));
    for (int i=0; i<len; i++) 
        arr[i] = rand();
}

void print_arr(int arr[], int len) {
    printf("[");
    for (int i=0; i<len-1; i++)
        printf("%d, ", arr[i]);
    printf("%d]\n", arr[len-1]);
}
int is_equal(int arr[], int brr[], int len) {
    for (int i=0; i<len-1; i++)
        if (arr[i] != brr[i])
            return 0;
    return 1;
}
