import java.util.Scanner;

public class Main{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        int i = 1; //循环变量
        while(i <= n) { //循环条件
            //循环体
            System.out.println(i);
            i = i + 1;
        }
    }
}
