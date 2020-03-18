import java.util.Scanner;

public class Main{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int score = input.nextInt();
        if (score >= 90)
            System.out.println("A");
        else if (score >=80)
            System.out.println("B");
        else if (score >=70)
            System.out.println("C");
        else if (score >=60)
            System.out.println("D");
        else
            System.out.println("E");
        /*
        int a = 10;
        int b = 5;
        if (a > 7) {
            System.out.println("a>7");
        } else {
            System.out.println("a<=7");
        }

        if (b < 7) {
            System.out.println("b<7");
        } else {
            System.out.println("b>=7");
        }
        */
    }
}
