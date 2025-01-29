import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Main {
    static List<Integer> toBase(int n, int base) {
        List<Integer> res = new ArrayList<>();
        while (n > 0) {
            res.add(n % base);
            n /= base;
        }
        Collections.reverse(res);
        return res;
    }

    static boolean isPalindrome(List<Integer> s) {
        int len = s.size();
        for (int i = 0; i < len / 2; i++) {
            if (!s.get(i).equals(s.get(len - 1 - i))) {
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while (t-- > 0) {
            int n = Integer.parseInt(br.readLine());
            boolean found = false;

            for (int base = 2; base <= 64; base++) {
                if (isPalindrome(toBase(n, base))) {
                    found = true;
                    break;
                }
            }
            sb.append(found ? 1 : 0).append("\n");
        }
        System.out.print(sb);
        br.close();
    }
}
