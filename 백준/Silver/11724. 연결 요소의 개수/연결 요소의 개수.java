import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] graph; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            graph[x][y] = 1; 
            graph[y][x] = 1;
        }

        int cnt = 0; 

        for (int j = 1; j <= n; j++) { 
            if (!visited[j]) { 
                cnt++;
                dfs(j);
            }
        }

        System.out.println(cnt);
    }

    static void dfs(int v) {
        visited[v] = true;

        for (int i = 1; i <= n; i++) { 
            if (graph[v][i] == 1 && !visited[i]) { 
                dfs(i);
            }
        }
    }
}
