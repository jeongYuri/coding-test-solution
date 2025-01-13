import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int cnt = 0;
        char[] eat = br.readLine().toCharArray();
        for(int i=0;i<n;i++){
            if(eat[i]=='P'){
                for(int j = Math.max(0,i-k);j<Math.min(n,i+k+1);j++){
                    if(eat[j]=='H'){
                        cnt++;
                        eat[j]='0';
                        break;
                    }
                }
            }
        }
        System.out.println(cnt);

    }
}
