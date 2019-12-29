#include <stdio.h>
#include <limits.h>
#include "../include/algo_util.h"

const int len = 10000;
int orr[len];
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
        *leftIndex=rli, *rightIndex=rri, *maxSum=rmax;
//        if(rmax==*maxSum)
 //          printf("%d, %d, %d\n", rli, rri, rmax);
        if(cmax>=*maxSum)
            *leftIndex=cli, *rightIndex=cri, *maxSum=cmax;
  //      if(cmax==*maxSum)
   //        printf("%d, %d, %d\n", cli, cri, cmax);
        if(lmax>=*maxSum) 
            *leftIndex=lli, *rightIndex=lri, *maxSum=lmax;
        /*
        if(lmax>=rmax && lmax>=cmax) 
            *leftIndex=lli, *rightIndex=lri, *maxSum=lmax;
        else if(rmax>=lmax && rmax>=cmax)
            *leftIndex=rli, *rightIndex=rri, *maxSum=rmax;
        else {
            *leftIndex=cli, *rightIndex=cri, *maxSum=cmax;
        }
        if(lmax==*maxSum)
           printf("%d, %d, %d\n", lli, lri, lmax);
        else if(rmax==*maxSum)
           printf("%d, %d, %d\n", rli, rri, rmax);
        else if(cmax==*maxSum)
           printf("%d, %d, %d\n", cli, cri, cmax);
           */
    }
}

int main(){
    printf("%d\n", len);
    init_rand_ints(orr, len);
    for (int i=0; i<len; i++){
        orr[i] = orr[i]%56 + 45;
    }
    for (int i=0; i<len; i++){
        printf("%d ", orr[i]);
    }
    printf("\n");
    /*
    for (int i=1; i<len; i++){
        arr[i] = orr[i-1]-orr[i];
    }
    print_arr(arr, len);
    for (int i=0;i<5;i++){
       scanf("%d", orr+i);
    }
    print_arr(orr, len);
    */
    for (int i=1; i<len; i++){
        arr[i] = orr[i-1]-orr[i];
    }
    //print_arr(arr, len);

    int l, r, m = -9999;
    find_max_subarray(arr, 0, len-1, &l, &r, &m);
    printf("%d %d %d\n", l?l:1, r+1, m);

/*
    find_max_cross_array(arr, 0, 1, 3, &l, &r, &m);
    printf("%d, %d, %d\n", l, r, m);
    find_max_cross_array(arr, 0, 4, 9, &l, &r, &m);
    printf("%d, %d, %d\n", l, r, m);
    */
    return 0;
}
