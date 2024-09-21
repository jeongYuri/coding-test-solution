import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        
        int minPrime = Integer.MAX_VALUE;
        int sum = 0;

        for (int i = m; i <= n; i++) {
            if (isPrime(i)) {
                minPrime = Math.min(minPrime, i);
                sum += i;
            }
        }

        if (sum == 0) {
            System.out.println(-1);
        } else {
            System.out.println(sum);
            System.out.println(minPrime);
        }
    }

    static boolean isPrime(int num) {
        if (num < 2) return false; // 0과 1은 소수가 노놉
        for (int j = 2; j * j <= num; j++) { 
            if (num % j == 0) return false;
        }
        return true;
    }
}