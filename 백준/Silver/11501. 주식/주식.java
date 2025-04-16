import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc= Integer.parseInt(br.readLine());
        while(tc-->0){
            int n = Integer.parseInt(br.readLine());
            String[]input = br.readLine().split(" ");
            int[] numbers = new int[n];
            for(int i = 0;i<n;i++){
                numbers[i] = Integer.parseInt(input[i]);
            }
            long profit = 0;
            int max = 0;

            for(int i = n-1;i>=0;i--){
                if(numbers[i]>max){
                    max = numbers[i];
                }else{
                    profit += max-numbers[i];
                }
            }
            System.out.println(profit);



        }
        
    }
}
    
