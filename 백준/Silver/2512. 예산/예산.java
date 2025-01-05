import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine()); 
        int[] arr = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        int maxBudget = 0; 
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            maxBudget = Math.max(maxBudget, arr[i]); 
        }
        int totalBudget = Integer.parseInt(br.readLine()); 
        int start = 0, end = maxBudget, result = 0;

        while (start <= end) {
            int mid = (start + end) / 2; 
            long sum = 0; 

            for (int i = 0; i < n; i++) {
                if (arr[i] > mid) {
                    sum += mid; 
                } else {
                    sum += arr[i]; 
                }
            }

            if (sum <= totalBudget) {
                result = mid; 
                start = mid + 1; 
            } else {
                end = mid - 1; 
            }
        }

        System.out.println(result);
    }
}
