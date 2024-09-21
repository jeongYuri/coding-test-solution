import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int cnt = (x < 100) ? x : 99; 

        for (int i = 100; i <= x; i++) {
            int h = i / 100; //백
            int t = (i / 10) % 10;//십 
            int o = i % 10; //일~@!
            if (h - t == t - o) {
                cnt++;
            }
        }
        System.out.println(cnt);
    }
}
