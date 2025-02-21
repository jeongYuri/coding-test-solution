import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String[] inputs = br.readLine().split(" ");
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputs[i]);  
        }

        long Lcnt = 0;
        long Rcnt = 0;
        long sum = 0;
        int idx = 0;

        for(int i = 0;i<n;i++){
            int num = arr[i];
            if(num %2==0){
                sum += idx++;
                Lcnt +=i;
                Rcnt += n-1-i;
            }
        }
        System.out.println(Math.min(Lcnt, Rcnt) - sum);
    }
}