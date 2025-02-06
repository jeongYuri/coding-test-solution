import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        TreeMap<Integer, Integer> mosq = new TreeMap<>();

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            int e = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());

            mosq.put(e, mosq.getOrDefault(e, 0) + 1); // 모기 들어옴
            mosq.put(x, mosq.getOrDefault(x, 0) - 1); // 모기 나감
        }

        int maxMos = -1, mosSum = 0;
        int start = -1, end = -1;
        boolean check = false;

        for (int time : mosq.keySet()) {
            mosSum += mosq.get(time);

            if (mosSum > maxMos) {
                maxMos = mosSum;
                start = time;
                check = true;
            }

            if (mosSum < maxMos && check) {
                end = time;
                check = false;
            }
        }

        if (check) {
            end = mosq.lastKey();
        }

        System.out.println(maxMos);
        System.out.println(start + " " + end);
    }
}
