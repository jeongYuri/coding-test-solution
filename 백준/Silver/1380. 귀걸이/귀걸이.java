import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = 1;
        
        while (true) {
            int n = Integer.parseInt(br.readLine().trim());
            if (n == 0) break;

            List<String> names = new ArrayList<>();
            Set<Integer> goods = new HashSet<>();

            for (int i = 0; i < n; i++) {
                names.add(br.readLine().trim());
            }

            for (int i = 0; i < 2 * n - 1; i++) {
                String[] input = br.readLine().split(" ");
                int num = Integer.parseInt(input[0]);
                
                if (goods.contains(num)) {
                    goods.remove(num);
                } else {
                    goods.add(num);
                }
            }

            int remaining = goods.iterator().next(); 
            System.out.println(cnt + " " + names.get(remaining - 1)); 

            cnt++;
        }
    }
}