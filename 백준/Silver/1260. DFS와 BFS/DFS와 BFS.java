import java.io.*;
import java.util.*;

public class Main {
    public static void dfs(List<List<Integer>>graph, boolean[]visited,int v){
        visited[v] = true; //현재 노드 방문 처리
        System.out.print(v + " ");
        for (int next:graph.get(v)){
            if(!visited[next]){
                dfs(graph,visited, next);
            }
        }
    }
    public static void bfs(List<List<Integer>>graph, boolean[]visited, int start){
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(start);
        visited[start] = true;
        while(!queue.isEmpty()){
            int v = queue.poll();
            System.out.print(v+" ");
            for (int next:graph.get(v)){
                if(!visited[next]){
                    queue.offer(next);
                    visited[next] = true;
                }
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0;i<=n;i++){
            graph.add(new ArrayList<>());
        }
        for (int i=0;i<m;i++){ //간선 정보 입력
            st = new StringTokenizer(br.readLine());
            int u = Integer.parseInt(st.nextToken());
            int v = Integer.parseInt(st.nextToken());
            graph.get(u).add(v);
            graph.get(v).add(u);
        }
        for(int i=1;i<=n;i++){ //연결된 리스트 오름차순
            Collections.sort(graph.get(i));
        }
        boolean[] visited = new boolean[n+1];
        dfs(graph,visited, start);
        System.out.println();

        visited = new boolean[n+1];
        bfs(graph, visited, start);
        System.out.println(); //줄바꿈

    
    
    
    }

}