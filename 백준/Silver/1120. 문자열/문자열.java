
import java.util.TreeMap;
import java.util.Scanner;
import java.util.StringTokenizer;
public class Main {

     public static void main(String[] args) {
          Scanner sc = new Scanner(System.in);
          
          String x = sc.next();
          String y = sc.next();
          int minDiff = Integer.MAX_VALUE;
          for(int i=0;i<=y.length()-x.length();i++){
               int diff = 0;
               for(int j=0;j<x.length();j++){
                    if(x.charAt(j)!=y.charAt(i+j)){
                         diff++;
                    }
               }
               minDiff = Math.min(minDiff, diff);
          }
          System.out.println(minDiff);
          sc.close();
     }
     
}