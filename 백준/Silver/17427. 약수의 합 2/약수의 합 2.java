import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        long[] f =  new long[n+1];
        for(int i = 1;i<=n;i++){
            for(int j = i;j<=n;j+=i){
                f[j]+=i;
            }
        }
        long g = 0;
        for(int i = 1;i<=n;i++){
            g+=f[i];
        }
        System.out.println(g);
    }
}