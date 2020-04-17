import java.io.File;

public class CreateNewFile{
    public static void main(String[] args) throws Exception{
        if (args.length != 0) {
            File file = new File(args[0]);
            if (!file.exists())
                file.createNewFile();
        } else {
            System.out.println("Please input the FileName as CMD parameter.");
        }
    }
}
