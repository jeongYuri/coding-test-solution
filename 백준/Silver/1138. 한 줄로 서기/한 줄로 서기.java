import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int n = Integer.parseInt(br.readLine());
        String[] list = br.readLine().split(" ");
        int[] people = new int[n];
        int[] res = new int[n];
        Arrays.fill(res,0);
        for(int i=0;i<n;i++){
            people[i] = Integer.parseInt(list[i]);
        }
        for(int i=0;i<n;i++){
            int cnt = 0;
            for(int j = 0;j<n;j++){
                if(res[j]==0){
                    cnt ++;
                }
                if(cnt == people[i]+1){
                    res[j] = i+1;
                    break;
                }
            }
        }
        for(int num:res){
            System.out.print(num+" ");
        }
        
    }
}
