import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Integer[] tip = new Integer[n];
        for(int i = 0;i<n;i++){
            tip[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(tip, Collections.reverseOrder());
        long ans = 0;
        for(int i = 0;i<n;i++){
            int temp = tip[i]-i;
            if (temp>0){
                ans+=temp;
            }
        
        }
        System.out.println(ans);
    }
    
}

