import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int i = 0;i<t;i++){
            int cnt = 0; //0의 개수 찾아야함..~
            StringTokenizer st = new StringTokenizer(br.readLine());

            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());

            for(int k = n;k<=m;k++){
                int num = k;
                if(num==0){
                    cnt++;
                }
                while(num>0){
                    if(num%10==0){
                        cnt++;
                    }
                    num/=10;
                }
            }
            System.out.println(cnt);
        }
    }
}