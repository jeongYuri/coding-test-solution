import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int s = sc.nextInt();
        int[] stair = new int[s+1];
        int[] dp = new int[s+1];
        
        for (int i = 1; i <= s; i++){
            stair[i] = sc.nextInt();
        }
        
        dp[1] = stair[1];
        if (s > 1) {
            dp[2] = stair[1] + stair[2];
        }
        
        for (int i = 3; i <= s; i++){
            dp[i] = Math.max(dp[i-2] + stair[i], dp[i-3] + stair[i-1] + stair[i]);
        }
        
        System.out.println(dp[s]);
    }
}