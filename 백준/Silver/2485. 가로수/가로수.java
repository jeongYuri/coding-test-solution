
import java.util.Scanner;
import java.util.Arrays;
public class Main {

     public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          
          int n = sc.nextInt();
          int[] trees = new int[n];
          for(int i=0;i<n;i++){
               trees[i] = sc.nextInt();
          }
          Arrays.sort(trees);
          int[] gaps = new int[n-1];
          for(int i=0;i<n-1;i++){
               gaps[i] = trees[i+1]-trees[i];
          }
          int gcd = gaps[0];
          for(int i=1;i<gaps.length;i++){
               gcd = getGCD(gcd, gaps[i]);
          }
          int res = 0;
          for(int gap:gaps){
               res += (gap/gcd)-1;
          }
          
          System.out.println(res);
     }
     private static int getGCD(int a, int b){
          if(b==0){
               return a;
          }
          return getGCD(b,a%b);
     }
     
}