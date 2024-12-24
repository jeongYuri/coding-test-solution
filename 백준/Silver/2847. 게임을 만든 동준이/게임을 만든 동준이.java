
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {

     public static void main(String[] args) throws IOException {
          BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
          int n = Integer.parseInt(br.readLine());
          int[] scores = new int[n];
          for(int i=0;i<n;i++){
               scores[i] = Integer.parseInt(br.readLine());
          }
       
          int cnt = 0;
          for(int i = n-2; i>=0;i--){
               if (scores[i]>=scores[i+1]){
                    int decrease = scores[i]-scores[i+1]+1;
                    scores[i] -= decrease;
                    cnt += decrease;

               }
          }
          System.out.println(cnt);
     }
}