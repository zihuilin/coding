import java.util.Scanner;

public class TiCe{

    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        int gen = input.nextInt();
        int grade = input.nextInt();
        int minute = input.nextInt();
        int second = input.nextInt();
        int time = minute*60 * second;
        
        if (gen == 1){ //girl
           if (grade == 12){
            if (time > 4*60+32)
                System.out.println(0);
            else if (time > 3*60+42)
                System.out.println(1);
            else if (time > 3*60+27)
                System.out.println(2);
            else
                System.out.println(3);
           }else{ //34
           if (grade == 12){
            if (time > 4*60+30)
                System.out.println(0);
            else if (time > 3*60+40)
                System.out.println(1);
            else if (time > 3*60+25)
                System.out.println(2);
            else
                System.out.println(3);
           }
        }else{ //boy
           if (grade == 12){
            if (time > 4*60+32)
                System.out.println(0);
            else if (time > 3*60+42)
                System.out.println(1);
            else if (time > 3*60+27)
                System.out.println(2);
            else
                System.out.println(3);
           }else{ //34
           if (grade == 12){
            if (time > 4*60+30)
                System.out.println(0);
            else if (time > 3*60+40)
                System.out.println(1);
            else if (time > 3*60+25)
                System.out.println(2);
            else
                System.out.println(3);
           }
        }

    }
}
