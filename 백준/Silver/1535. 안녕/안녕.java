import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String [] inputs = br.readLine().split(" ");
        String [] inputs2 = br.readLine().split(" ");
        
        int []p = new int[n];
        int []h = new int[n];
        int[] dp = new int[100];

        for(int i = 0;i<n;i++){
            p[i] = Integer.parseInt(inputs[i]);
            h[i] = Integer.parseInt(inputs2[i]);
        }

        for(int i = 0;i<n;i++){
            for (int j = 99; j >= p[i]; j--) {
                dp[j] = Math.max(dp[j],dp[j-p[i]]+h[i]);
            }
        }
        int maxHappy = 0;
        for (int i = 0; i < 100; i++) {
            maxHappy = Math.max(maxHappy, dp[i]);
        }
        System.out.println(maxHappy);
    }
   
}
