import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] numbers = new int[n];
        int[] dp = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            numbers[i] = Integer.parseInt(st.nextToken());
            dp[i] = numbers[i];
        }
        for(int i=0;i<n;i++){
            for(int j=0;j<i;j++){
                if(numbers[i]>numbers[j]){
                    dp[i] = Math.max(dp[i],dp[j]+numbers[i]);
                }
            }
        }
        int max  = 0;
        for(int value: dp){
            max = Math.max(max, value);
        }
        System.out.println(max);
        }
        }
    

