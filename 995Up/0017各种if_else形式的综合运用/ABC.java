import java.util.Scanner;

public class ABC{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int max = a;
        int b = input.nextInt();
        if (b > max)
            max = b;
        int c = input.nextInt();
        if (c > max)
            max = c;
        System.out.println(max);

        /*
        if (a >= b){
            if (a >= c){
                System.out.println(a);
            }
        }
        else if (b >= a){
            if (b >= c){
                System.out.println(b);
            }
        }
        else if (c >= b){
            if (c >= a){
                System.out.println(c);
            }
        }
        */
    }
}
