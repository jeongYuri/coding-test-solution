import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] radii = new int[n];
        for(int i=0;i<n;i++){
          radii[i] = sc.nextInt();
        }
        int firstr = radii[0];
        for(int i=1;i<n;i++){
          int gcd = gcd(firstr, radii[i]);
          System.out.println((firstr/gcd)+"/" +(radii[i]/gcd));
        }
        sc.close();
        }
     private static int gcd(int a, int b){
          if(b==0){
               return a;
          }
          return gcd(b,a%b);
     }
 }

