public class Main{
    public static boolean isLeapYear(int year){
        if((year%4==0 && year%100!=0) || year%400==0)
            return true;
        else
            return false;
    }

    public static int gcd(int num1, int num2){
        int big = num1 > num2 ? num1 : num2;
        int small = num1 < num2 ? num1 : num2;
        while (big%small!=0){
            int r = big%small;
            big = small;
            small = r;
        }
        return small;
    }

    public static void main(String[] args){
        int g = gcd(24, 8);
        System.out.println(g);
        /*
        System.out.println(isLeapYear(1900));
        boolean ily = isLeapYear(2000);
        if (ily)
            System.out.println("2000年是闰年");
        else
            System.out.println("2000年不是闰年");
       */
    }
}
