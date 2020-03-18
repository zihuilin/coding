import java.util.Scanner;
public class Main{
    public static void fun(int num){
        if (num < 0) {
            System.out.println("Hello, 小于0");
            return;
        }
        System.out.println("Hello, 大于或等于0");
    }

    public static int max(int param1, int param2){
        int result = 0;
        if (param1 > param2) {
            System.out.println("max is: " + param1);
            result = param1;
        }
        else {
            System.out.println("max is: " + param2);
            result = param2;
        }
        return result;
    }

    public static void main(String[] args){
        System.out.println( max(10, 5) );
        //fun(-10);
        //System.out.println("Hello");
        //return;
        //System.out.println("after return");
    }
}
