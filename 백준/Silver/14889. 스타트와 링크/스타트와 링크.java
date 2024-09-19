import java.util.Scanner;

public class Main {
    static int N;
    static int[][] ability;
    static boolean[] visited;
    static int minDifference = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        N = sc.nextInt();
        ability = new int[N][N];
        visited = new boolean[N];

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                ability[i][j] = sc.nextInt();
            }
        }

        backtrack(0, 0);
        System.out.println(minDifference);
    }

    static void backtrack(int index, int count) {
        if (count == N / 2) {
            calculateDifference();
            return;
        }

        for (int i = index; i < N; i++) {
            if (!visited[i]) {
                visited[i] = true;
                backtrack(i + 1, count + 1);
                visited[i] = false;
            }
        }
    }

    static void calculateDifference() {
        int startTeam = 0;
        int linkTeam = 0;

        for (int i = 0; i < N - 1; i++) {
            for (int j = i + 1; j < N; j++) {
                if (visited[i] && visited[j]) {
                    startTeam += ability[i][j] + ability[j][i];
                } else if (!visited[i] && !visited[j]) {
                    linkTeam += ability[i][j] + ability[j][i];
                }
            }
        }

        int difference = Math.abs(startTeam - linkTeam);
        minDifference = Math.min(minDifference, difference);
    }
}