import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int x = Integer.parseInt(st.nextToken());

        List<List<Integer>> graph = new ArrayList<>();
        for(int i = 0;i<=n;i++){
            graph.add(new ArrayList<>());
        }
        for(int i = 0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            graph.get(a).add(b); // a번 도시에서 b번 도시로 이동
        }
        int[]distance = new int[n+1];
        Arrays.fill(distance, -1);
        distance[x] = 0;

        Queue<Integer> q = new LinkedList<>();
        q.offer(x);//출발 도시를 q에 cnrk

        while(!q.isEmpty()){
            int now = q.poll();
            for(int next_city:graph.get(now)){
                if(distance[next_city]==-1){
                    distance[next_city] = distance[now]+1;
                    q.offer(next_city);
                }
            }
        }
        List<Integer> res = new ArrayList<>();
        for(int i = 1;i<=n;i++){
            if(distance[i]==k){
                res.add(i);
            }
        }
        if(!res.isEmpty()){
            Collections.sort(res);
            for(int city:res){
                System.out.println(city);
            }
        }else{
            System.out.println(-1);
        }
    }     
}
    
