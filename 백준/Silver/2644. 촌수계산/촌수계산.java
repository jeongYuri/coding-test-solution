import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

import org.xml.sax.SAXException;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(br.readLine());
        
        //그래프 초기화
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0;i<=n;i++){
            graph.add(new ArrayList<>());
        }

        boolean[]visited = new boolean[n+1];
        List<Integer> result = new ArrayList<>();
        

        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            
            graph.get(x).add(y);
            graph.get(y).add(x);
        }

        dfs(graph, visited,result, a,b,0);
        if(result.isEmpty()){
            System.out.println(-1);
        }else{
            System.out.print(result.get(0)-1);
        }
    }
    static void dfs(List<List<Integer>> graph, boolean[] visited,List<Integer> result, int v, int target, int cnt){
        cnt +=1;
        visited[v] = true;
        if(v==target){
            result.add(cnt);
            return;
        }
        for(int next:graph.get(v)){
            if(!visited[next]){
                dfs(graph, visited, result, next, target,cnt);
            }
        }
    }
}