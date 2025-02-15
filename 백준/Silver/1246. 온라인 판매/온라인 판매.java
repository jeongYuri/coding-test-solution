import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int [] prices = new int[m];
        for(int i = 0;i<m;i++){
            prices[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(prices);

        int maxRevenue = 0;
        int bestPrices = 0;

        for(int i = 0;i<m;i++){
            int price = prices[i];
            int buyers = Math.min(n,m-i);
            int revenue = price* buyers;

            if(revenue>maxRevenue){
                maxRevenue = revenue;
                bestPrices = price;
            }
        }
        System.out.println(bestPrices+" "+ maxRevenue);
    }
}
