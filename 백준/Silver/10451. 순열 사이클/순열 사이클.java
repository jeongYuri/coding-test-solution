
import java.util.Scanner;
import java.util.StringTokenizer;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
public class Main {

     public static void main(String[] args) throws IOException {
          Scanner sc = new Scanner(System.in);
          int t = sc.nextInt();
          for(int i=0;i<t;i++){
               int n = sc.nextInt();
               int[] arr = new int[n+1];
               boolean[] visited = new boolean[n+1];

               for(int j = 1;j<=n;j++){
                    arr[j] = sc.nextInt();
               }
               int cnt = 0;
               for(int k = 1;k<=n;k++){
                    if(!visited[k]){
                         dfs(k,arr,visited);
                         cnt++;
                    }
               }
               System.out.println(cnt);
          }
          sc.close();
     }
     private static void dfs(int node, int[]arr, boolean[]visited){
          visited[node] = true;
          int nextnode = arr[node];
          if(!visited[nextnode]){
               dfs(nextnode,arr, visited);
          }
     }
}