import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        int d = scanner.nextInt();

        List<Integer> res = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            if (i >= 10) {
                String numStr = Integer.toString(i);
                for (char c : numStr.toCharArray()) {
                    res.add(Character.getNumericValue(c));
                }
            } else {
                res.add(i);
            }
        }
        int count = 0;
        for (int num : res) {
            if (num == d) {
                count++;
            }
        }

        System.out.println(count);
    }
}