import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] score = new int[n];
        String[] lines = br.readLine().split(" ");
        for(int i = 0;i<n;i++){
            score[i] = Integer.parseInt(lines[i]);
        }
        int max = score[0];
        for (int i = 1; i < n; i++) {
            if (score[i] > max) {
                max = score[i];
            }
        }
        double sum = 0;
        for(int i = 0;i<n;i++){
            
            double newScore = (score[i] / (double)max) * 100;
            sum += newScore;
            
           
        }
        double res = sum / n;
        System.out.println(res);
    
        
    }
}
    
