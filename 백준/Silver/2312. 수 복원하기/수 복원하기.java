import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t= Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();

        while(t-->0){
            int n = Integer.parseInt(br.readLine());
            Map<Integer,Integer> cnt = new LinkedHashMap<>();

            while(n%2==0){
                cnt.put(2,cnt.getOrDefault(2,0)+1);
                n/=2;
            }
            for (int i = 3; i * i <= n; i += 2) {
                while (n % i == 0) {
                    cnt.put(i, cnt.getOrDefault(i, 0) + 1);
                    n /= i;
                }
            }
            if (n > 1) {
                cnt.put(n, 1);
            }
            for (Map.Entry<Integer, Integer> entry : cnt.entrySet()) {
                sb.append(entry.getKey()).append(" ").append(entry.getValue()).append("\n");
            }
        }
        System.out.print(sb.toString());
    }
    }
