import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[11];
        dp[1] = 0;
        dp[2] = 1;
        for(int i = 3; i <= n; i++){
            for(int j = 1; j <= i/2; j++){
                dp[i] = Math.max(dp[i], j*(i-j) + dp[j] + dp[i-j]);
            }
        }
        System.out.println(dp[n]);
    }
}