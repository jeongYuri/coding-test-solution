import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //동기수
        int m = Integer.parseInt(br.readLine()); //리스트의 길이이
        ArrayList<Integer>[] graph = new ArrayList[n+1];
        for(int i = 0;i<=n;i++) graph[i] = new ArrayList<>();
        for(int i = 0;i<m;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
        
            graph[a].add(b);
            graph[b].add(a);
        }
        boolean[] visited = new boolean[n+1];
        Queue<Integer>q = new LinkedList<>();
        int[] depth = new int[n+1];

        q.add(1);
        visited[1] = true;
        int cnt = 0;

        while(!q.isEmpty()){
            int now = q.poll();
            for(int next:graph[now]){
                if(!visited[next]){
                    depth[next] = depth[now]+1;
                    if(depth[next]<=2){
                        cnt++;
                        visited[next] = true;
                        q.add(next);
                    }
                }
            }
        }
        System.out.println(cnt);

            
            
        
    }
}
    
