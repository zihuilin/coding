import java.util.Scanner;
public class Main{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();

        if (a<10)
            a = -a;

        System.out.println(a%10);
        System.out.println((a/10)%10);
        System.out.println((a/100)%10);
    }
}
