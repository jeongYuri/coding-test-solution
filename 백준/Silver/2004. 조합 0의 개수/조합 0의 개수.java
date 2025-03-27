import java.io.*;
import java.util.*;

public class Main {
    static int factorial(int n, int p){
        int cnt = 0;
        while(n>=p){
            cnt += n/p;
            n/=p;
        }
        return cnt;
    }
    static int zero(int n, int m){
        int two = factorial(n,2)-factorial(m,2)-factorial(n-m,2);
        int five = factorial(n,5)-factorial(m,5)-factorial(n-m,5);
        return Math.min(two,five);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        System.out.println(zero(n,m));
    }    
    
    
}
    
