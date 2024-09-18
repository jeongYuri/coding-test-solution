import java.io.*;
import java.util.*;

public class Main {
    static int N, M;
    static int[][] office;
    static List<CCTV> cctvList = new ArrayList<>();
    static int[] dx = {-1, 0, 1, 0};
    static int[] dy = {0, 1, 0, -1};
    static int minSpot = Integer.MAX_VALUE;

    static class CCTV {
        int x, y, type;
        CCTV(int x, int y, int type) {
            this.x = x;
            this.y = y;
            this.type = type;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        office = new int[N][M];

        for (int i = 0; i < N; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < M; j++) {
                office[i][j] = Integer.parseInt(st.nextToken());
                if (office[i][j] >= 1 && office[i][j] <= 5) {
                    cctvList.add(new CCTV(i, j, office[i][j]));
                }
            }
        }

        dfs(0, office);
        System.out.println(minSpot);
    }

    static void dfs(int index, int[][] map) {
        if (index == cctvList.size()) {
            minSpot = Math.min(minSpot, countSpot(map));
            return;
        }

        CCTV cctv = cctvList.get(index);
        int[][] newMap = new int[N][M];

        for (int dir = 0; dir < 4; dir++) {
            for (int i = 0; i < N; i++) {
                newMap[i] = map[i].clone();
            }
            watch(cctv, dir, newMap);
            dfs(index + 1, newMap);
        }
    }

    static void watch(CCTV cctv, int dir, int[][] map) {
        switch (cctv.type) {
            case 1: watchDirection(cctv.x, cctv.y, dir, map); break;
            case 2: 
                watchDirection(cctv.x, cctv.y, dir, map);
                watchDirection(cctv.x, cctv.y, (dir + 2) % 4, map);
                break;
            case 3: 
                watchDirection(cctv.x, cctv.y, dir, map);
                watchDirection(cctv.x, cctv.y, (dir + 1) % 4, map);
                break;
            case 4: 
                watchDirection(cctv.x, cctv.y, dir, map);
                watchDirection(cctv.x, cctv.y, (dir + 1) % 4, map);
                watchDirection(cctv.x, cctv.y, (dir + 2) % 4, map);
                break;
            case 5: 
                for (int i = 0; i < 4; i++) {
                    watchDirection(cctv.x, cctv.y, i, map);
                }
                break;
        }
    }

    static void watchDirection(int x, int y, int dir, int[][] map) {
        while (true) {
            x += dx[dir];
            y += dy[dir];
            if (x < 0 || x >= N || y < 0 || y >= M || map[x][y] == 6) break;
            if (map[x][y] == 0) map[x][y] = -1;
        }
    }

    static int countSpot(int[][] map) {
        int count = 0;
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (map[i][j] == 0) count++;
            }
        }
        return count;
    }
}