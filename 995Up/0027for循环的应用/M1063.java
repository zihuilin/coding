import java.util.Scanner;

public class M1063 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int i = 0;
        for (i=2; i<=n; i++){
            if (n%i == 0)
                break;
        }
        if (i == n)
            System.out.println("prime");
        else 
            System.out.println("no prime");
    }
}
