import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        long[] distances = new long[n-1];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n-1; i++) {
            distances[i] = Long.parseLong(st.nextToken());
        }
        
        long[] prices = new long[n];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            prices[i] = Long.parseLong(st.nextToken());
        }
        
        long totalCost = 0;
        long minPrice = prices[0];
        
        for (int i = 0; i < n-1; i++) {
            if (prices[i] < minPrice) {
                minPrice = prices[i];
            }
            totalCost += minPrice * distances[i];
        }
        
        System.out.println(totalCost);
    }
}