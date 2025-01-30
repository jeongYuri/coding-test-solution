import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n];
        String[] num = br.readLine().split(" ");
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(num[i]);
        }
        long[] prefix_sum = new long[n+1];
        Arrays.fill(prefix_sum,0);

        for(int i=1;i<n+1;i++){
            prefix_sum[i] = prefix_sum[i-1]+arr[i-1];
        }
        long res = 0;
        for(int i=0;i<n;i++){
            res += (long)arr[i]*(prefix_sum[n]-prefix_sum[i+1]);
        }
        System.out.println(res);
    }
}