import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for(int k=0;k<t;k++){
            String[] input  = br.readLine().split(" ");
            int stn = Integer.parseInt(input[0]);
            int[] heights = new int[input.length-1];
            for(int i=1;i<input.length;i++){
                heights[i-1] = Integer.parseInt(input[i]);
            }
            int total = 0;
            for(int i=0;i<heights.length-1;i++){
                for(int j=i+1;j<heights.length;j++){
                    if(heights[i]>heights[j]){
                        int tmp = heights[i];
                        heights[i] = heights[j];
                        heights[j] = tmp;
                        total++;
                    }
                }
            }
            sb.append(stn).append(" ").append(total).append("\n");
        }
        System.out.print(sb);
    }
}