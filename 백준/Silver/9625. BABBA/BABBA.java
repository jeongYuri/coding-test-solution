import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int a = 1;
        int b = 0;
        for(int i=0;i<n;i++){
            int temp = a;
            a = b;
            b = temp+b;
        }
        System.out.print (a+" "+b);
    }
    
}
