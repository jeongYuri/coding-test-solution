import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String[] inputs = br.readLine().split(" ");
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(inputs[i]); 
        }
        int[] cnt = new int[2];
        int[] cntLeft = new int[2];

        for(int a: arr){
            int idx = a%2;
            cnt[idx]++;
            cntLeft[idx] += cnt[1-idx];
        }
        System.out.println(Math.min(cntLeft[0], cntLeft[1]));

        }
    }

