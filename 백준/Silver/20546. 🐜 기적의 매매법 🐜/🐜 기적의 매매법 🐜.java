import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] graph; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cash = Integer.parseInt(br.readLine());
        ArrayList<Integer> prices  = new ArrayList<>();
        String[] input = br.readLine().split(" ");
        for (String s : input) {
            prices.add(Integer.parseInt(s));
        }
        int bnp_cash = cash;
        int bnp_stock = 0;
        for(int i = 0;i<prices.size();i++){
            int price = prices.get(i);
            if(bnp_cash>=price){
                int buy = bnp_cash/price;
                bnp_stock+= buy;
                bnp_cash-= buy*price;
            }
        }
        int bnp_total = bnp_cash+bnp_stock*prices.get(prices.size()-1);

        int timing_cash = cash;
        int timing_stock = 0;
        int up_cnt = 0;
        int down_cnt =0;

        for(int i=0;i<prices.size();i++){
            if(i>0){
                if(prices.get(i)>prices.get(i-1)){
                    up_cnt++;
                    down_cnt = 0;
                }else if(prices.get(i)<prices.get(i-1)){
                    down_cnt++;
                    up_cnt = 0;
                }else{
                    up_cnt = 0;
                    down_cnt = 0;
                }
            }
            if(up_cnt>=3 && timing_stock>0){
                timing_cash += timing_stock*prices.get(i);
                timing_stock =0;
            }else if(down_cnt>=3 && timing_cash>=prices.get(i)){
                int buy = timing_cash/prices.get(i);
                timing_stock += buy;
                timing_cash -= buy*prices.get(i);
            }
        }
        int total_timing = timing_cash+timing_stock*prices.get(prices.size()-1);
       
       if(bnp_total>total_timing){
        System.out.println("BNP");
       }else if(bnp_total<total_timing){
        System.out.println("TIMING");
       }else{
        System.out.println("SAMESAME");
       }
    }
}

