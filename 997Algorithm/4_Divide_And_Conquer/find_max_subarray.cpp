#include <stdio.h>
#include "../include/algo_util.h"

const int len = 10;
int arr[len];

void find_max_cross_array
    (int a[], int low, int mid, int height, 
        int* leftIndex, int* rightIndex, int* maxSum){
   int lIndex = mid, lmax = a[mid], lcurrent=lmax;
   for (int i=mid-1; i>=low; i--){
       lcurrent += a[i];
       if (lcurrent>lmax){
           lIndex = i;
           lmax = lcurrent;
       }
   }

   int rIndex = mid+1, rmax = a[mid+1], rcurrent=rmax;
   for (int i=mid+2; i<=height; i++){
       rcurrent += a[i];
       if (rcurrent>rmax){
           rIndex = i;
           rmax = rcurrent;
       }
   }
   *leftIndex = lIndex; *rightIndex = rIndex; *maxSum = lmax + rmax;
}

void find_max_subarray(int a[], int low, int height,
        int* leftIndex, int* rightIndex, int* maxSum){
    if (low==height) 
        *leftIndex=low, *rightIndex=low, *maxSum=a[low];
    else {
        int mid = (height + low)/2;
        int lli, lri, lmax; find_max_subarray(a, low, mid, &lli, &lri, &lmax);
        int rli, rri, rmax; find_max_subarray(a, mid+1, height, &rli, &rri, &rmax);
        int cli, cri, cmax; find_max_cross_array(a, low, mid, height, &cli, &cri, &cmax);
        if(lmax>=rmax && rmax>=cmax)
            *leftIndex=lli, *rightIndex=lri, *maxSum=lmax;
        else if(rmax>=lmax && rmax>=cmax)
            *leftIndex=rli, *rightIndex=rri, *maxSum=rmax;
        else 
            *leftIndex=cli, *rightIndex=cri, *maxSum=cmax;
    }
}

int main(){
    init_rand_ints(arr, len);
    for (int i=0; i<len; i++){
        arr[i] = arr[i]%100 - 50;
    }
    print_arr(arr, len);
    int l, r, m;
    find_max_subarray(arr, 0, 9, &l, &r, &m);
    printf("%d, %d, %d\n", l, r, m);

    /*
    find_max_cross_array(arr, 0, 1, 3, &l, &r, &m);
    printf("%d, %d, %d\n", l, r, m);
    find_max_cross_array(arr, 0, 4, 9, &l, &r, &m);
    printf("%d, %d, %d\n", l, r, m);
    */
    return 0;
}
