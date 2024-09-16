import java.util.Scanner;
import java.util.Arrays;
import java.util.Collections;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        Integer [] coins = new Integer[n];
        for(int i=0;i<n;i++){
            coins[i] = sc.nextInt();
        }
        Arrays.sort(coins, Collections.reverseOrder());
        int count = 0;
        for (int i=0;i<n;i++){
            if(m>=coins[i]){
                count += m/coins[i];
                m%=coins[i];
            }
        }
        System.out.println(count);
        sc.close();
    }
}