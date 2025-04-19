import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); //횡단보도
        int k = Integer.parseInt(st.nextToken()); //최소 신호등? 
        int b = Integer.parseInt(st.nextToken()); //고장난 신호등 갯수수

        int[] cross = new int[n+2];
       
        for(int i = 0;i<b;i++){
            int broken = Integer.parseInt(br.readLine());
            cross[broken] = 1;
        }

        //System.out.println(Arrays.toString(list));
        int fix = 0; //수리할 신호등 개수
        for(int i = 1;i<=k;i++){
            fix += cross[i];
        }
        int min = fix;
        
        for(int i = k+1;i<=n;i++){
            fix = fix + cross[i] - cross[i-k];
            min = Math.min(min, fix);
        }
        System.out.println(min);
    }
}
    
