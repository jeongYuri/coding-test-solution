import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[]args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int [] share = new int[n];
    
        for(int i=0;i<n;i++){
            share[i] = Integer.parseInt(br.readLine());
        }
        Arrays.sort(share);
        int start = 1, end = (share[n-1]-share[0]);
        int res = 0;
        while(start<=end){
            int mid = start+(end-start)/2;
            int cnt = 1;
            int home = share[0];
            for(int i=1;i<n;i++){
                if (share[i]-home>=mid){
                    cnt++;
                    home = share[i];
                }
            }
            if(cnt>=m){
                res = mid;
                start = mid+1;
            }else {
                end = mid-1;
            }
            
        }
        System.out.println(res);
    }
}