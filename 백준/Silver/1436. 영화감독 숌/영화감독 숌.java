import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 0;
        int result = 666;
        
        while (true) {
            if (String.valueOf(result).contains("666")) {
                cnt++;
            }
            if (cnt == n) {
                break;
            }
            result++;
        }
        
        System.out.println(result);
        sc.close();
    }
}