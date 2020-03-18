public class M1010{
    public static void main(String[] args){
        int i = 1;
        while (i <= 1000){
            if (i%10==0 && i%3!=0)
                System.out.println(i);
            i++;
        }
    }
}
