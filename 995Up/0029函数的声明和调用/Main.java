public class Main{
    public static int max (int param1, int param2){
        int result = param1;
        if (param2 > result)
            result = param2;
        return result;
    }
    public static void main(String[] args){
        int a = 10, b = 5;
        int m = max(a, b);
        System.out.println( m );
    }
}
