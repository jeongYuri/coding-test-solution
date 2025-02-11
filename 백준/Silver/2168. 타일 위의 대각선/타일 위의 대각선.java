import java.util.Scanner;

public class Main {
    public static int gcd(int x, int y) {
        if (y == 0) {
            return x;
        }
        return gcd(y, x % y);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int x = scanner.nextInt();
        int y = scanner.nextInt();
        scanner.close();
        
        int max = Math.max(x, y);
        int min = Math.min(x, y);
        
        int result = max + min - gcd(max, min);
        System.out.println(result);
    }
}