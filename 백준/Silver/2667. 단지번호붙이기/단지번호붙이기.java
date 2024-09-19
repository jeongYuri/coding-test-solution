import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] home;
    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());  
        home = new int[n][n];  
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < n; j++) {
                home[i][j] = line.charAt(j) - '0';
            }
        }

        List<Integer> res = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (home[i][j] == 1) {
                    cnt = 0;
                    dfs(i, j);
                    res.add(cnt);
                }
            }
        }

        Collections.sort(res);
        System.out.println(res.size());
        for (int r : res) {
            System.out.println(r);
        }
    }

    static void dfs(int x, int y) {
        if (x < 0 || x >= n || y < 0 || y >= n || home[x][y] == 0) return;
        home[x][y] = 0;
        cnt++;
        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];
            dfs(nx, ny);
        }
    }
}