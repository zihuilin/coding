
public class Main{
    public static void main(String[] args){
        char genda = 'F';
        int hairLength = 5;

        boolean isBoy = genda == 'M';
        boolean longHair = hairLength > 5;

        System.out.println(isBoy ^ longHair);
    }

}
