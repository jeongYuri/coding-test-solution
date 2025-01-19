import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        long[][] dp = new long[n+1][10];
        final int MOD = 1000000000;
        
        for (int i = 1; i <= 9; i++) {
            dp[1][i] = 1;
        }
   
        for (int i = 2; i <= n; i++) {
            for (int j = 0; j <= 9; j++) {
                if (j == 0) {
                    dp[i][j] = dp[i-1][1];
                } else if (j == 9) {
                    dp[i][j] = dp[i-1][8];
                } else {
                    dp[i][j] = (dp[i-1][j-1] + dp[i-1][j+1]) % MOD;
                }
            }
        }

        long res = 0;
        for (int i = 0; i <= 9; i++) {
            res = (res + dp[n][i]) % MOD;
        }
        
        System.out.println(res);
    }
}