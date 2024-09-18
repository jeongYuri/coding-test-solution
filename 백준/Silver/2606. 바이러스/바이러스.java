import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n= Integer.parseInt(br.readLine());
        int c = Integer.parseInt(br.readLine());
        List<List<Integer>> graph = new ArrayList<>();
        for(int i=0;i<=n;i++){
            graph.add(new ArrayList<>());
        }
        for(int i=0;i<c;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b);
            graph.get(b).add(a);
        }
        boolean [] visited = new boolean[n+1];
        Queue<Integer>queue = new LinkedList<>();
        queue.offer(1);
        visited[1] = true;
        int cnt = 0;
        while(!queue.isEmpty()){
            int current = queue.poll();
            for(int next : graph.get(current)){
                if(!visited[next]){
                    queue.offer(next);
                    visited[next] = true;
                    cnt++;
                }
            }
        }

        System.out.println(cnt);
    }
}