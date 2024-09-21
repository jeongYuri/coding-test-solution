import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int A = sc.nextInt();
        int B = sc.nextInt();
        int K = sc.nextInt();

        A = A % B; 
        for (int i = 0; i < K - 1; i++) {
            A = (A * 10) % B; 
        }

        int res = (A * 10) / B;
        System.out.println(res);
    }
}
