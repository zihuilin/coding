import java.util.Scanner;

public class Prime{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        for (int i=2; i<=n; i++){
            int j=2;
            for (; j<=i; j++){
                if (i%j==0)
                    break;
            }
            if (j==i)
                System.out.println(i);
        }
    }
}
