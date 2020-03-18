import java.util.Scanner;
public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int a = input.nextInt();
        int max = a;
        int b = input.nextInt();
        max = b>max ? b : max;
        int c = input.nextInt();
        max = c>max ? c : max;
        System.out.println(max);
        //int x = 10;
        //int y = x>0 ? 1 : 2;
        //System.out.println(x>0 ? "x大于0" : "x不大于0");
    }
}
