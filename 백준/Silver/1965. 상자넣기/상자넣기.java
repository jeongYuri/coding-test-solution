import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] box = new int[n];
        String[] list = br.readLine().split(" ");
        for(int i=0;i<n;i++){
            box[i] = Integer.parseInt(list[i]);
        }
        int[] dp = new int[n];
        Arrays.fill(dp,1);
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                if(box[j]<box[i]){
                    dp[i] = Math.max(dp[i],dp[j]+1);
                }
            }
        }
        int res = 0;
        for(int i = 0; i < n; i++){
            res = Math.max(res, dp[i]);
        }
        System.out.println(res);
    }
}
