import java.util.Scanner;

public class M1205{
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        long n = input.nextLong();
        boolean dThree = n%3==0;
        boolean dFive = n%5==0;
        boolean dSeven = n%7==0;
        if (dThree && dFive && dSeven)
            System.out.println("Nice");
        else if (dThree && dFive)
            System.out.println("3和5");
        else if (dSeven && dFive)
            System.out.println("5和7");
        else if (dThree && dSeven)
            System.out.println("3和7");
        else if (dThree)
            System.out.println("3");
        else if (dSeven)
            System.out.println("7");
        else if (dFive)
            System.out.println("5");
        else
            System.out.println("No");
    }
}
