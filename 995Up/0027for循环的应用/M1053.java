import java.util.Scanner;

public class M1053 {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int m = input.nextInt();
        int n = input.nextInt();
        float f = m, s = 0;
        for (int i=1; i<=n; i++){
            s = s + f;
            f = f / 2;
            s = s + f;
        }
        System.out.printf("%.2f %.2f", f, s-f);
    }
}
