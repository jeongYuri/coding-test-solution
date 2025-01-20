import java.util.*;
import java.io.*;

public class Main {
    static int n;
    static ArrayList<ArrayList<Node>> arr;
    static boolean[] visited;
    static long[] d;
    static long lcm = 1;

    static class Node {
        int to, p, q;
        Node(int to, int p, int q) {
            this.to = to;
            this.p = p;
            this.q = q;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        arr = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            arr.add(new ArrayList<>());
        }
        visited = new boolean[n];
        d = new long[n];

        for (int i = 0; i < n - 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int p = Integer.parseInt(st.nextToken());
            int q = Integer.parseInt(st.nextToken());
            arr.get(a).add(new Node(b, p, q));
            arr.get(b).add(new Node(a, q, p));
            lcm *= (long) p * q / gcd(p, q);
        }

        d[0] = lcm;
        dfs(0);

        long mgcd = d[0];
        for (int i = 1; i < n; i++) {
            mgcd = gcd(mgcd, d[i]);
        }

        for (int i = 0; i < n; i++) {
            System.out.print(d[i] / mgcd + " ");
        }
    }

    static long gcd(long a, long b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    static void dfs(int v) {
        visited[v] = true;
        for (Node node : arr.get(v)) {
            if (!visited[node.to]) {
                d[node.to] = d[v] * node.q / node.p;
                dfs(node.to);
            }
        }
    }
}