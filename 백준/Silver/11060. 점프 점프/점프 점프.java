import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] lines = br.readLine().split(" ");
        int[] map = new int[n];
        for(int i = 0;i<n;i++){
            map[i] = Integer.parseInt(lines[i]);
        }

        int []dist = new int[n];
        Arrays.fill(dist, -1);

        Queue<Integer> q = new LinkedList<>();
        q.add(0);
        dist[0] = 0;

        while(!q.isEmpty()){
            int now  = q.poll();
            int jump = map[now];

            for(int i = 1;i<=jump;i++){
                int next = now+i;
                if(next<n && dist[next]==-1){
                    dist[next] = dist[now]+1;
                    q.add(next);
                }
            }
        }
        System.out.println(dist[n-1]);
        
    }
}
    
