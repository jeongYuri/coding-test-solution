import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        for(int t=1;t<=k;t++){
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int[] scores = new int[n];

            for(int i=0;i<n;i++){
                scores[i] = Integer.parseInt(input[i+1]);
            }
            Arrays.sort(scores);
            int maxScore = scores[n - 1];
            int minScore = scores[0];
            int largestGap = 0;
            for (int i = 0; i < n - 1; i++) {
                largestGap = Math.max(largestGap, scores[i + 1] - scores[i]);
            }
         
            System.out.println("Class " + t);
            System.out.println("Max " + maxScore + ", Min " + minScore + ", Largest gap " + largestGap);
        }
    }
}

