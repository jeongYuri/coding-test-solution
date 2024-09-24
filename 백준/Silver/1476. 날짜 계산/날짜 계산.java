import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int E = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        int year = 1, e = 1, s = 1, m = 1;
        while (true) {
            if (e == E && s == S && m == M) {
                break;
            }
            year++;
            e = (e % 15) + 1;
            s = (s % 28) + 1;
            m = (m % 19) + 1;
        }

        System.out.println(year);
    }
}
