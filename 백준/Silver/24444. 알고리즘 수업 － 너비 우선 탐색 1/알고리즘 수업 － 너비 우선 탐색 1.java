import java.io.*;
import java.util.*;

public class Main {
    static ArrayList<Integer>[] graph;
    static int[] visited;
    static int cnt = 1; 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());

        graph = new ArrayList[n+1]; //그래프 초기화
        visited = new int[n+1]; //방문 배열 초기화

        for(int i = 1;i<=n;i++){
            graph[i] = new ArrayList<>();
        }

        for(int i = 0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph[u].add(v);
            graph[v].add(u);
        }
        for(int i = 1;i<=n;i++){
            Collections.sort(graph[i]);
        }
        bfs(r);
        for(int i =1;i<=n;i++){
            System.out.println(visited[i]);
        }
    }
    static void bfs(int start){
       Queue<Integer> q = new LinkedList<>();
       q.add(start);
       visited[start] = cnt++;
        while(!q.isEmpty()){
            int now = q.poll();
            for(int next: graph[now]){
                if(visited[next]==0){
                    visited[next] = cnt++;
                    q.add(next);
                }
            }
        }
    }
    
}
    
