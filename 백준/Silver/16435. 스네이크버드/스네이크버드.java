import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());
        int [] high = new int[n];
        String[] list = br.readLine().split(" ");
        
        for(int i=0;i<n;i++){
            high[i] = Integer.parseInt(list[i]);
        }
        Arrays.sort(high);
        for(int i=0;i<n;i++){
            if (high[i]<= l){
                l++;
            }else{
                break;
            }
        }
        System.out.println(l);
        
    }
}
