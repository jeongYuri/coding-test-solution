import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] dp = new int[n];
        Arrays.fill(dp, 1);
        int[]arr = new int[n];
        StringTokenizer st  = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                if(arr[i]<arr[j]){
                    dp[i] = Math.max(dp[i], dp[j]+1);
                }
            }
        }
        int res = Arrays.stream(dp).max().getAsInt();
        System.out.println(res);
        }

    }

