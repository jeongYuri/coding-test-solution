import java.io.*;
import java.util.*;

public class Main {
    static String input;
    static List<int[]> indices = new ArrayList<>();
    static Set<String> ans = new TreeSet<>();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        input = br.readLine().trim();
        
        Stack<Integer> stack = new Stack<>();
 
        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '(') {
                stack.push(i);
            } else if (input.charAt(i) == ')') {
                if (!stack.isEmpty()) {
                    indices.add(new int[]{stack.pop(), i});
                }
            }
        }

        int n = indices.size();
        for (int i = 1; i <= n; i++) {
            generateCombinations(new boolean[n], 0, i);
        }

        for (String s : ans) {
            System.out.println(s);
        }
    }

    private static void generateCombinations(boolean[] selected, int start, int r) {
        if (r == 0) {
            removeParentheses(selected);
            return;
        }
        for (int i = start; i < indices.size(); i++) {
            selected[i] = true;
            generateCombinations(selected, i + 1, r - 1);
            selected[i] = false;
        }
    }
    private static void removeParentheses(boolean[] selected) {
        StringBuilder sb = new StringBuilder(input);
        for (int i = 0; i < indices.size(); i++) {
            if (selected[i]) {
                sb.setCharAt(indices.get(i)[0], '\0'); 
                sb.setCharAt(indices.get(i)[1], '\0');
            }
        }

        ans.add(sb.toString().replace("\0", ""));
    }
}
