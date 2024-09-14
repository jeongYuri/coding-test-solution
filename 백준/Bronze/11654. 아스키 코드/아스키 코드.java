import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            char text = sc.next().charAt(0);
            int ascii = (int)text;
            System.out.println(ascii);
            sc.close();
    }
    
}