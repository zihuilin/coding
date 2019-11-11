#include <stdio.h>
#include <string.h>
#include <algorithm>
#include "../include/algo_util.h"

const int len = 10;
int a[len];
int b[len];

void insert_sort(int arr[], int len){
    for (int i=1; i<len; i++){
        int key = arr[i];
        int j = i - 1;
        while (j>=0 && arr[j] > key){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = key;
    }
}

int main(){
    init_rand_ints(a, len);
    memcpy(b, a, len*sizeof(int));
    std::sort(b, b+len);
    insert_sort(a, len);
    if (is_equal(a, b, len))
        printf("ok\n");
    else
        printf("no!\n");
    return 0;
}
