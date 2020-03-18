public class SelectionSort {
    
    public static void selectionSort(int[] arr){
        for (int i=0; i<=arr.length-2; i++){
            int max = arr[i];
            int maxIndex = i;
            for (int j=i+1; j<arr.length; j++){
                if (arr[j] > max){
                    max = arr[j];
                    maxIndex = j;
                }
            }
            System.out.println(max + " at " + maxIndex);

            arr[maxIndex] = arr[i];
            arr[i] = max;
        }
    }

    public static void main(String[] args){
        int[] a = {7, 4, 2, 9, 5, 8, 1, 6, 3};
        selectionSort(a);
    }
}
