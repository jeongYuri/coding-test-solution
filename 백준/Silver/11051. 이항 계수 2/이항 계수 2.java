import java.io.*;
import java.util.*;

public class Main {
    static final int MOD = 10007;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        long[] factorial = new long[n + 1];
        factorial[0] = 1;
        for (int i = 1; i <= n; i++) {
            factorial[i] = (factorial[i - 1] * i) % MOD;
        }

        long res = (factorial[n] * modInverse(factorial[k], MOD) % MOD * modInverse(factorial[n - k], MOD) % MOD) % MOD;
        System.out.println(res);
    }

    private static long modInverse(long a, int mod) {
        return power(a, mod - 2, mod);
    }

    private static long power(long base, int exp, int mod) {
        long result = 1;
        while (exp > 0) {
            if (exp % 2 == 1) {
                result = (result * base) % mod;
            }
            base = (base * base) % mod;
            exp /= 2;
        }
        return result;
    }
}
