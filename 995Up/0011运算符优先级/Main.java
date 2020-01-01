public class Main{

    public static void main(String[] args){
        int x = 5;
        int y = 10;
        int z = ++x * y--; //z:60, x:6, y:9
        System.out.println(x + " " + y + " " + z);
        z = -3*-x; //z:18
        System.out.println(x + " " + y + " " + z);
        z = z-y*2; //z:0
        System.out.println(x + " " + y + " " + z);
        z = (z+19)/(x-1); //z:3
        System.out.println(x + " " + y + " " + z);
    }
}
