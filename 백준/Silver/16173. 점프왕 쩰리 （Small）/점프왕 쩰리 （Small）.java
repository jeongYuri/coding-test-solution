import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] game;
    static int[][] directions = {{0, 1}, {1, 0}};  

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine()); 

        game = new int[n][n];

        // 게임판 입력 받기
        for (int i = 0; i < n; i++) {
            String[] line = br.readLine().split(" ");  
            for (int j = 0; j < n; j++) {
                game[i][j] = Integer.parseInt(line[j]);
            }
        }

        bfs();  // BFS로 경로 탐색
    }

    static void bfs() {
        Queue<int[]> q = new LinkedList<>();
        Set<String> visited = new HashSet<>();

        q.add(new int[]{0, 0});  // 시작 위치
        visited.add("0,0");

        while (!q.isEmpty()) {
            int[] pos = q.poll();
            int x = pos[0], y = pos[1];

            if (game[x][y] == -1) {  // 승리 조건
                System.out.println("HaruHaru");
                return;
            }

            int step = game[x][y];  // 이동할 칸 수
            for (int[] dir : directions) {
                int nx = x + dir[0] * step;
                int ny = y + dir[1] * step;

                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    String key = nx + "," + ny;
                    if (!visited.contains(key)) {
                        visited.add(key);
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
        System.out.println("Hing");  // 탈출 불가능한 경우
    }
}
