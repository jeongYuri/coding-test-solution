import java.io.*;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    static ArrayList<ArrayList<Integer>> friend;
    static int[] visited;
    static int n,m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
         m = Integer.parseInt(st.nextToken());

        friend = new ArrayList<>();
        for(int i=0;i<=n;i++){
            friend.add(new ArrayList<>());
        }

        for(int i=0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            friend.get(a).add(b);
            friend.get(b).add(a);
        }

        int bacon = Integer.MAX_VALUE;
        int res = 0;

        for(int i=1;i<=n;i++){
            visited = new int[n+1];
            int sum = bfs(i);
            if(sum<bacon){
                bacon = sum;
                res =i;
            }
        }
        System.out.println(res);
    }

    static int bfs(int start){
        Queue<Integer> q = new LinkedList<>();
        q.offer(start);
        visited[start] = 1;
        int sum = 0;

        while(!q.isEmpty()){
            int s= q.poll();
            for(int i:friend.get(s)){
                if(visited[i]==0){
                    visited[i] = visited[s]+1;
                    q.offer(i);
                }
            }
        }
        for(int i=1;i<=n;i++){
            sum+= visited[i]-1;
        }
        return sum;
    }
        
        
}
