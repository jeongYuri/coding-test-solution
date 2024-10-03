import java.io.*;
import java.util.*;
import java.util.regex.*;;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int ball = 1;
        for(int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            if (ball == x){
                ball = y;
            }else if(ball==y){
                ball = x;
            }
        }
        System.out.println(ball);
        br.close();
    }
}
