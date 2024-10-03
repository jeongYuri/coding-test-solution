import java.io.*;
import java.util.*;
import java.util.regex.*;;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int ans  = 0;
        int cnt = 0;
        for(int i=0;i<4;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int off = Integer.parseInt(st.nextToken());
            int on = Integer.parseInt(st.nextToken());
            cnt += on-off;
            ans = Math.max(ans,cnt); 
        }
        System.out.println(ans);
    }
}
