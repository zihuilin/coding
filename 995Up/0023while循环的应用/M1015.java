import java.util.Scanner;

public class M1015{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        long n = input.nextLong();
        n = n<0 ? -n : n;
        while (n!=0) {
            System.out.println(n%10);
            n = n/10;
        }
    }
}
