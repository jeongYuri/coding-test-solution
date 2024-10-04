import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        boolean found = false;

        for (int i = l; i <= 100; i++) { 
            int x = n - (i * (i - 1) / 2);
            if (x % i == 0) {
                x = x / i;
                if (x >= 0) {
                    found = true;
                    for (int j = 0; j < i; j++) {
                        System.out.print((x + j) + " ");
                    }
                    break;
                }
            }
        }

        if (!found) {
            System.out.println("-1");
        }
    }
}