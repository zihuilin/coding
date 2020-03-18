public class Main{

    public static void list(int[] array){
        for(int i=0; i<array.length; i++){
            System.out.println(array[i]);
        }
    }

    public static int[] copy(int[] array){
        int[] newArray = new int[array.length];

        for(int i=0; i<array.length; i++){
            newArray[i] = array[i];
        }
        return newArray;
    }

    public static void main(String[] args){
        int[] scores = {1, 2, 3, 7, 8, 9, 4, 5, 6};


        //int[] scores2 = scores;
        int[] scores2 = copy(scores);
        scores[0] = 10;
        list(scores2);
        /*
        for(int i=0; i<scores.length; i++){
            System.out.println(scores[i]);
        }
        */
    }
}
