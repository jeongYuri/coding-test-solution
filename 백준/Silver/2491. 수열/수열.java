import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        int[] arr = new int[n];
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        int inc = 1;
        int dec = 1;
        int length = 1;
        for(int i=1;i<n;i++){
            if(arr[i]>=arr[i-1]){
                inc ++;
            }else{
                inc = 1;
            }
            if(arr[i]<=arr[i-1]){
                dec ++;
            }else{
                dec = 1;
            }
            length = Math.max(length, Math.max(dec,inc));
        }
     System.out.println(length);  
    }
}

    

