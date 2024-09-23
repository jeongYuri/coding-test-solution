import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int cur = 64; 
        int cnt = 0; 
      
        while (x > 0) {
            if (cur > x) {
                cur /= 2; 
            } else {
                cnt++; 
                x -= cur; 
            }
        }
        
        System.out.println(cnt); 
    }
}
