import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        int [] visitors = new int[n];
        String[] inputs = br.readLine().split(" ");
        for(int i = 0;i<n;i++){
            visitors[i] = Integer.parseInt(inputs[i]);
        }

        long currentSum =0;
        for(int i = 0;i<x;i++){
            currentSum+=visitors[i];
        }

        long maxSum = currentSum;
        int cnt = 1;
        
        for(int i =x;i<n;i++){
            currentSum = currentSum - visitors[i-x]+visitors[i];

            if(currentSum>maxSum){
                maxSum = currentSum;
                cnt =1;
            }else if(currentSum == maxSum){
                cnt ++;
            }
        }
        if(maxSum==0){
            System.out.println("SAD");
        }else{
            System.out.println(maxSum);
            System.out.println(cnt);
        }

    }
}
