import java.util.Scanner;

public class Main{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int ll = input.nextInt();
        int mj = input.nextInt();

        if (ll > 50){
            if(mj > 50){
                System.out.println(3);
            } else {
                System.out.println(1);
            }
        } else {
            if(mj > 50){
                System.out.println(2);
            } else {
                System.out.println(4);
            }
        }

    }
}
