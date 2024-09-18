import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br =  new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int lcm = findlcm(n,m);
        int gcd = findgcd(n,m);
        System.out.println(gcd);
        System.out.println(lcm);
        
    }
    public static int findgcd(int n,int m){
        while(m!=0){
            int temp = m;
            m = n%m;
            n = temp;
        }
        return n;

    }
    public static int findlcm(int n, int m){
        return (n*m)/findgcd(n, m);

    }

}