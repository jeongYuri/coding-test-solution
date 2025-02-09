import java.io.*;
import java.util.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc= Integer.parseInt(br.readLine());
        for(int t = 0;t<tc;t++){
            int n = Integer.parseInt(br.readLine());
            String[] inputs = br.readLine().split(" ");
            int[] arr = new int[n];
            for(int i =0;i<n;i++){
                arr[i] =Integer.parseInt(inputs[i]);
            }

            int[] dp = new int[n];
            dp[0] =arr[0];
            for (int i = 1; i < n; i++) {
                dp[i] = Math.max(arr[i],dp[i-1]+arr[i]);
            }
            int maxSum = dp[0];
            for(int i =1;i<n;i++){
                maxSum = Math.max(maxSum, dp[i]);
            }
            System.out.println(maxSum);
        }
    }
           
}

