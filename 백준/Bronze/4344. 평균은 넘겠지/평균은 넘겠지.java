import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        for(int i = 0;i<tc;i++){
            String [] line = br.readLine().split(" ");
            int n = Integer.parseInt(line[0]);
            int[] score = new int[n];
            int hab = 0;
            for(int j = 0;j<n;j++){
                score[j] = Integer.parseInt(line[j+1]);
                hab+=score[j];
            }
            double avg = (double)hab/n;
            int cnt = 0;
            for(int k = 0;k<n;k++){
                if(score[k]>avg){
                    cnt++;
                }
            }
            double res = ((double)cnt/n)*100;
            System.out.printf("%.3f%%\n", res);
        }
        
    }
}
    
