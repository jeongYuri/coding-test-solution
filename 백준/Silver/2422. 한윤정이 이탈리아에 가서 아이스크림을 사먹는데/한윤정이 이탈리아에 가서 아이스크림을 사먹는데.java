import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 아이스크림 종류 수
        int m = Integer.parseInt(st.nextToken()); // 싫어하는 조합 개수

        Map<Integer, Set<Integer>> hate = new HashMap<>();
        for (int i = 1; i <= n; i++) {
            hate.put(i, new HashSet<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            hate.get(a).add(b);
            hate.get(b).add(a);
        }

        int count = 0;
        for (int i = 1; i <= n - 2; i++) {
            for (int j = i + 1; j <= n - 1; j++) {
                for (int k = j + 1; k <= n; k++) {
                    if (!hate.get(i).contains(j) && !hate.get(i).contains(k) && !hate.get(j).contains(k)) {
                        count++;
                    }
                }
            }
        }

        System.out.println(count);
    }
}