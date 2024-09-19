import java.io.*;
import java.util.*;

public class Main {
    static int m, n; 
    static int[][] tomato;
    static Queue<int[]> q = new LinkedList<>();
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        m = Integer.parseInt(st.nextToken()); // 가로
        n = Integer.parseInt(st.nextToken()); // 세로
        tomato = new int[n][m];

        for(int i = 0; i < n; i++){ 
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++){ 
                tomato[i][j] = Integer.parseInt(st.nextToken());
                if(tomato[i][j] == 1){
                    q.offer(new int[]{i, j});
                }
            }
        }
        System.out.println(bfs());
    }

    static int bfs(){
        while (!q.isEmpty()) {
            int[] current = q.poll();
            int x = current[0];
            int y = current[1];
            for (int i = 0; i < 4; i++){
                int nx = x + dx[i];
                int ny = y + dy[i];
                if(0 <= nx && nx < n && 0 <= ny && ny < m && tomato[nx][ny] == 0){ 
                    q.offer(new int[]{nx, ny});
                    tomato[nx][ny] = tomato[x][y] + 1;
                }
            }
        }

        int max = 0;
        for(int i = 0; i < n; i++){
            for (int j = 0; j < m; j++){
                if(tomato[i][j] == 0) return -1;
                max = Math.max(max, tomato[i][j]);
            }
        }
        return max - 1;
    }
}