import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

public class Main {

    public static void bfs(int x, int y, int[][] island, boolean[][] visited, int w, int h) {
        int[] dx = {-1, 1, 0, 0, -1, -1, 1, 1};
        int[] dy = {0, 0, -1, 1, -1, 1, -1, 1};

        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[y][x] = true;

        while (!q.isEmpty()) {
            int[] current = q.poll();
            int cx = current[0];
            int cy = current[1];

            for (int i = 0; i < 8; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && nx < w && ny >= 0 && ny < h && !visited[ny][nx] && island[ny][nx] == 1) {
                    visited[ny][nx] = true;
                    q.add(new int[]{nx, ny});
                }
            }
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] dimensions = br.readLine().split(" ");
            int w = Integer.parseInt(dimensions[0]);
            int h = Integer.parseInt(dimensions[1]);

            if (w == 0 && h == 0) {
                break;
            }

            int[][] island = new int[h][w];
            boolean[][] visited = new boolean[h][w];

            for (int i = 0; i < h; i++) {
                String[] row = br.readLine().split(" ");
                for (int j = 0; j < w; j++) {
                    island[i][j] = Integer.parseInt(row[j]);
                }
            }

            int count = 0;

            for (int y = 0; y < h; y++) {
                for (int x = 0; x < w; x++) {
                    if (island[y][x] == 1 && !visited[y][x]) {
                        bfs(x, y, island, visited, w, h);
                        count++;
                    }
                }
            }

            System.out.println(count);
        }
    }
}
