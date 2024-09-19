import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            int n = Integer.parseInt(br.readLine());
            int[][]candiates = new int[n][2];
            for(int j=0;j<n;j++){
                StringTokenizer st = new StringTokenizer(br.readLine());
                candiates[j][0] = Integer.parseInt(st.nextToken());
                candiates[j][1] = Integer.parseInt(st.nextToken());
            }
            Arrays.sort(candiates,(a,b)->a[0]-b[0]);
            int cnt = 1;
            int mininterview = candiates[0][1];
            for(int i=0;i<n;i++){
                if(candiates[i][1]<mininterview){
                    cnt ++;
                    mininterview = candiates[i][1];
                }
            }
            System.out.println(cnt);
        }
    }
}