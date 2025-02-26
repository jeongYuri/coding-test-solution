import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] ranking = new int[n];

        for(int i = 0;i<n;i++){
            ranking[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(ranking);

        long total = 0;
        for(int i = 0;i<n;i++){
            total += Math.abs(ranking[i]-(i+1));
        }
        System.out.println(total);
    }
}
