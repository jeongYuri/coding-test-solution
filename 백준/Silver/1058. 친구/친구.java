import java.io.*;
import java.util.*;

public class Main {
       public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        char[][] friend = new char[n][n];
        for(int i=0;i<n;i++){
            friend[i] = br.readLine().toCharArray();
        }
        
        int maxcnt = 0;
        for(int i=0;i<n;i++){
            boolean[] visited = new boolean[n]; //각 탐색마다 초기화화
            visited[i] = true;
            Queue<int[]> q = new LinkedList<>();
            q.add(new int[]{i,0});

            int cnt = 0;
            while(!q.isEmpty()){
                int[] cur = q.poll();
                int node = cur[0];
                int depth = cur[1];
                if(depth==2) continue;
                for(int k=0;k<n;k++){
                    if(friend[node][k]=='Y' && !visited[k]){
                        visited[k]= true;
                        q.add(new int[]{k,depth+1});
                        cnt++;
                    }
                }
            }
            maxcnt = Math.max(maxcnt, cnt);
        }
        System.out.println(maxcnt);
    }
}
