import java.io.*;
import java.util.*;

public class Main {
    static int t, ans, res;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        t = Integer.parseInt(br.readLine());
        for (int i = 0; i < t; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            ans = Integer.parseInt(st.nextToken());
            res = Integer.parseInt(st.nextToken());

            boolean[] visited = new boolean[10000];
            Queue<Register> q = new LinkedList<>();
            visited[ans] = true;
            q.add(new Register(ans, new StringBuilder()));

            while (!q.isEmpty()) {
                Register cur = q.poll();
                if (cur.num == res) {
                    sb.append(cur.cmd).append("\n");
                    break;
                }

                int nextD = cur.D();
                int nextS = cur.S();
                int nextL = cur.L();
                int nextR = cur.R();

                if (!visited[nextD]) {
                    visited[nextD] = true;
                    q.add(new Register(nextD, new StringBuilder(cur.cmd).append("D")));
                }
                if (!visited[nextS]) {
                    visited[nextS] = true;
                    q.add(new Register(nextS, new StringBuilder(cur.cmd).append("S")));
                }
                if (!visited[nextL]) {
                    visited[nextL] = true;
                    q.add(new Register(nextL, new StringBuilder(cur.cmd).append("L")));
                }
                if (!visited[nextR]) {
                    visited[nextR] = true;
                    q.add(new Register(nextR, new StringBuilder(cur.cmd).append("R")));
                }
            }
        }
        System.out.println(sb);
    }

    static class Register {
        int num;
        StringBuilder cmd;

        Register(int num, StringBuilder cmd) {
            this.num = num;
            this.cmd = cmd;
        }

        int D() {
            return (num * 2) % 10000;
        }

        int S() {
            return num == 0 ? 9999 : num - 1;
        }

        int L() {
            return num % 1000 * 10 + num / 1000;
        }

        int R() {
            return num % 10 * 1000 + num / 10;
        }
    }
}
