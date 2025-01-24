import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        double[] score = new double[n];
    
        for (int i = 0; i < n; i++) {
            score[i] = Double.parseDouble(br.readLine());
        }
        
        Arrays.sort(score);
        for (int i = 0; i < Math.min(7, n); i++) {
 
            System.out.printf("%.3f%n", score[i]);
        }
    }
}