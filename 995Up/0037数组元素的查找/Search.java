public class Search {
    
    public static void selectionSort(int[] arr){
        for (int i=0; i<=arr.length-2; i++){
            int min = arr[i];
            int minIndex = i;
            for (int j=i+1; j<arr.length; j++){
                if (arr[j] < min){
                    min = arr[j];
                    minIndex = j;
                }
            }
            arr[minIndex] = arr[i];
            arr[i] = min;
        }
    }

    public static int binarySearch(int[] a, int target){
        int left = 0;
        int right = a.length-1;

        while (left <= right) {
            int mid = (left + right) / 2;
            if (a[mid] == target)
                return mid;
            else if (a[mid] < target)
                left = mid + 1;
            else if (a[mid] > target)
                right = mid - 1;
        }
        return -1;
    }

    public static void main(String[] args){
        int[] a = {7, 4, 2, 9, 5, 8, 1, 6, 3};
        int target = 9;
        for(int i=0; i<a.length; i++){
            if(a[i] == target)
                System.out.println(i);
        }

        selectionSort(a);
        System.out.println(binarySearch(a, 9));

    }
}
