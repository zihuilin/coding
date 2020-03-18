import java.util.Scanner;

public class Prob{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int h = 0, t = 0;
        for (int i=1; i<=6; i++){
            for (int j=1; j<=6; j++){
                if((i+j)==n)
                    h++;
                if((i+j)==n && i==2)
                    t++;
            }
        }
        System.out.printf("%.2f%%\n", (float)t*100/h);
    }
}
