import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        int[][] tasty = new int[n][2];
      
        for(int i = 0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            tasty[i][0] = Integer.parseInt(st.nextToken());
            tasty[i][1] = Integer.parseInt(st.nextToken());
        }
        int minDiff = Integer.MAX_VALUE;

        for(int i = 1;i<(1<<n);i++){
            int sour = 1;
            int bitter = 0;

            for(int j = 0;j<n;j++){
                if((i&(1<<j))!=0){
                    sour *= tasty[j][0];
                    bitter += tasty[j][1];
                }
            }
            minDiff = Math.min(minDiff,Math.abs(sour-bitter));
        }
      
    System.out.println(minDiff);
    }
    
}
    
