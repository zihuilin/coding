public class Main{

    public static void main(String[] args){
        //int[] array; //数组的声明
        //array = {96, 98, 100};
        //array = new int[3];
        //int[] scores = {96, 98, 100};
        int[] scores = new int[3];

        int len = scores.length;
        System.out.println(len);

        int index = 1;
        scores[1] = 96;
        System.out.println(scores[index]);
    }
}
