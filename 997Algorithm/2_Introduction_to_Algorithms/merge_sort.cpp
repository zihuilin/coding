#include <stdio.h>
#include <string.h>
#include <algorithm>
#include "../include/algo_util.h"

const int len = 10;
int a[len];
int b[len];

void merge(int arr[], int s, int m, int e){
    int len1 = m - s + 1;
    int len2 = e - m;
    int brr[len1];
    int crr[len2];
    for (int i=0; i<len1; i++)
        brr[i] = arr[i+s];
    for (int i=0; i<len2; i++)
        crr[i] = arr[i+m+1];
    int i=0, j=0;
    for (int k=s; k<=e; k++){
        if (i<len1 && j<len2) {
            if (brr[i] > crr[j])
                arr[k] = crr[j++];
            else
                arr[k] = brr[i++];
        } else if (i == len1)
            arr[k] = crr[j++];
        else
            arr[k] = brr[i++];
    }
}

void _merge_sort(int arr[], int s, int e){
    if(s<e) {
        int m = (e+s)/2;
        _merge_sort(arr, s, m);
        _merge_sort(arr, m+1, e);
        merge(arr, s, m, e);
    }
}

void merge_sort(int arr[], int s, int e){
    _merge_sort(arr, s, e);
}

int main(){
    /*
    int a[] = {1,2};
    print_arr(a,2);
    merge(a,0,0,1);
    print_arr(a,2);
    */
    
    init_rand_ints(a, len);
    memcpy(b, a, len*sizeof(int));
    std::sort(b, b+len);
    merge_sort(a, 0, len-1);
    if (is_equal(a, b, len))
        printf("ok\n");
    else
        printf("no!\n");
    return 0;
}
