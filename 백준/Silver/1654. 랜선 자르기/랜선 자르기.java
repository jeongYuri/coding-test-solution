import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int k = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());
        int [] lensun = new int[k];
        long max = 0;
        for(int i=0;i<k;i++){
            lensun[i] = Integer.parseInt(br.readLine());
            max = Math.max(max,lensun[i]);
        }
        long start = 1;
        long end = max;
        while(start<=end){
            long mid = (start+end)/2;
            long line = 0;
            for(int i: lensun){
                line += i/mid;
            }
            if(line>=n){
                start = mid+1;
            }else{
                end = mid-1;
            }
        }
        
        System.out.println(end); 
    }
}