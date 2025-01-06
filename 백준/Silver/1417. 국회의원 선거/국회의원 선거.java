import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int dasom = Integer.parseInt(br.readLine());
        int[] candi = new int[n-1];
        int res = 0;
        for(int i=0;i<n-1;i++){
            candi[i] = Integer.parseInt(br.readLine());
        }
        if(n==1){
            System.out.println(0);
            return;
        }

        while(true){
            int maxIdx = 0;
            for(int i=1;i<candi.length;i++){
                if(candi[i]>candi[maxIdx]){
                    maxIdx = i;
                }
            }
            if(candi[maxIdx]<dasom)break;
            candi[maxIdx]-=1;
            dasom +=1;
            res+=1;
        }
        System.out.println(res);
    }
}
