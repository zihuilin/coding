#include <stdio.h>
#include <limits.h>
#include <stdlib.h>
#include <time.h>

const int maxlen = 100000;
float orr[maxlen];
float arr[maxlen];

void find_max_cross_array
    (float a[], int low, int mid, int height, 
        int* leftIndex, int* rightIndex, float* maxSum){
   int lIndex = mid; float lcurrent=a[mid]; float lmax = a[mid];
   for (int i=mid-1; i>=low; i--){
       lcurrent += a[i];
       if (lcurrent>lmax){
           lIndex = i;
           lmax = lcurrent;
       }
   }

   int rIndex = mid+1; float rcurrent=a[rIndex]; float rmax=rcurrent;
   for (int i=mid+2; i<=height; i++){
       rcurrent += a[i];
       if (rcurrent>rmax){
           rIndex = i;
           rmax = rcurrent;
       }
   }
   *leftIndex = lIndex; *rightIndex = rIndex; *maxSum = lmax + rmax;
}

void find_max_subarray(float a[], int low, int height,
        int* leftIndex, int* rightIndex, float* maxSum){
    if (low==height) 
        *leftIndex=low, *rightIndex=low, *maxSum=a[low];
    else {
        int mid = (height + low)/2;
        int lli, lri; float lmax; find_max_subarray(a, low, mid, &lli, &lri, &lmax);
        int rli, rri; float rmax; find_max_subarray(a, mid+1, height, &rli, &rri, &rmax);
        int cli, cri; float cmax; find_max_cross_array(a, low, mid, height, &cli, &cri, &cmax);
        *leftIndex=rli, *rightIndex=rri, *maxSum=rmax;
        if(cmax>=*maxSum)
            *leftIndex=cli, *rightIndex=cri, *maxSum=cmax;
        if(lmax>=*maxSum) 
            *leftIndex=lli, *rightIndex=lri, *maxSum=lmax;
        
    }
}

int main(){
    int len = 90000;
    printf("%d\n", len);
    srand(time(NULL));
    for (int i=0;i<len;i++){
       orr[i] = (float)(rand()%550000)/10000 + 45;
    }
    float max = orr[0];
    float min = orr[0];
    for (int i=0;i<len;i++){
       printf("%.4f ", orr[i]);
       if(orr[i]>max) max = orr[i];
       if(orr[i]<min) min = orr[i];
    }
       printf("\n");


    /*
    scanf("%d", &len);
   
    for (int i=0;i<len;i++){
       scanf("%f", orr+i);
    }
    */
    for (int i=1; i<len; i++){
        arr[i] = orr[i-1]-orr[i];
    }

    int l, r; float m = -9999;
    find_max_subarray(arr, 0, len-1, &l, &r, &m);
    printf("%d %d %.4f\n", l?l:1, r+1, m);
    printf("%.4f %.4f %.4f\n", orr[l?l-1:0], orr[r], m);
    printf("%.4f %.4f\n", max, min);

    return 0;
}
