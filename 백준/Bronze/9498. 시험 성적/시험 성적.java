import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        
        if (90 <= n && n <= 100) {
            System.out.print("A");
        } else if (80 <= n && n <= 89) {
            System.out.print("B");
        } else if (70 <= n && n <= 79) {
            System.out.print("C");
        } else if (60 <= n && n <= 69) {
            System.out.print("D");
        } else {
            System.out.print("F");
        }
        
        sc.close();
    }
}