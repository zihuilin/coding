public class Main{
    
    public static double max(double num1, double num2){
        if (num1 > num2)
            return num1;
        else
            return num2;
    }

    public static int max(int num1, int num2){
        if (num1 > num2)
            return num1;
        else
            return num2;
    }

    public static int max(int num1, int num2, int num3){
        return max(num1, max(num2, num3));
    }

    public static void main(String[] args){
        System.out.println(max(10,5));
        System.out.println(max(10,5,20));
        System.out.println(max(10.1,5.1));
    }
}
