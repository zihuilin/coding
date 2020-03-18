import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int num = 0, sum = 0;
        do {
            num = input.nextInt();
            if (num%2==0)
                continue;
            sum = sum + num;
            if (sum > 100)
                break;
        } while(true);
        System.out.println(sum);
    }
}
