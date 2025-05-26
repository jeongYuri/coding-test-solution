import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if (n == 0) {
            System.out.println(0);
            return;
        }

        StringBuilder res = new StringBuilder();

        while (n != 0) {
            int remainder = n % -2;

            if (remainder < 0) {
                remainder += 2;  
                n = n / -2 + 1;  
            } else {
                n = n / -2;
            }

            res.insert(0, remainder); 
        }

        System.out.println(res.toString());
    }
}
