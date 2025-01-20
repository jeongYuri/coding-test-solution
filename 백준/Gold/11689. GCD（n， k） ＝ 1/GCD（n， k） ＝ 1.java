import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        long n = scanner.nextLong();
        long result = eulerPhi(n);
        System.out.println(result);
        scanner.close();
    }

    public static long eulerPhi(long n) {
        long result = n;
        for (long p = 2; p * p <= n; p++) {
            if (n % p == 0) {
                result -= result / p;
                while (n % p == 0) {
                    n /= p;
                }
            }
        }
        if (n > 1) {
            result -= result / n;
        }
        return result;
    }
}