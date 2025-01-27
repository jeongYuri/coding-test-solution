import java.util.*;

public class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Map<Character, Integer> alpha = new HashMap<>();
        alpha.put('A', 3); alpha.put('B', 2); alpha.put('C', 1); alpha.put('D', 2); alpha.put('E', 4);
        alpha.put('F', 3); alpha.put('G', 1); alpha.put('H', 3); alpha.put('I', 1); alpha.put('J', 1);
        alpha.put('K', 3); alpha.put('L', 1); alpha.put('M', 3); alpha.put('N', 2); alpha.put('O', 1);
        alpha.put('P', 2); alpha.put('Q', 2); alpha.put('R', 2); alpha.put('S', 1); alpha.put('T', 2);
        alpha.put('U', 1); alpha.put('V', 1); alpha.put('W', 1); alpha.put('X', 2); alpha.put('Y', 2);
        alpha.put('Z', 1);

        int n = sc.nextInt();
        int m = sc.nextInt();
        String a = sc.next();
        String b = sc.next();
        
        List<Integer> names = new ArrayList<>();
        for (int i = 0; i < Math.min(n, m); i++) {
            names.add(alpha.get(a.charAt(i)));
            names.add(alpha.get(b.charAt(i)));
        }
        
        if (n > m) {
            for (int i = m; i < n; i++) {
                names.add(alpha.get(a.charAt(i)));
            }
        } else if (m > n) {
            for (int i = n; i < m; i++) {
                names.add(alpha.get(b.charAt(i)));
            }
        }

        while (names.size() > 2) {
            List<Integer> scores = new ArrayList<>();
            for (int i = 0; i < names.size() - 1; i++) {
                scores.add((names.get(i) + names.get(i + 1)) % 10);
            }
            names = scores;
        }

        int result = names.get(0) * 10 + names.get(1);
        System.out.println(result + "%");
    }
}
