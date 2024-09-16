import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Stack<Integer> stack = new Stack<>();
        
        int N = sc.nextInt();
        sc.nextLine();

        for (int i = 0; i < N; i++) {
            String input = sc.nextLine();
            String[] parts = input.split(" ");
            String command = parts[0];

            switch (command) {
                case "push":
                    int value = Integer.parseInt(parts[1]);
                    stack.push(value);
                    break;
                case "pop":
                    if (stack.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.pop());
                    }
                    break;
                case "size":
                    System.out.println(stack.size());
                    break;
                case "empty":
                    System.out.println(stack.isEmpty() ? 1 : 0);
                    break;
                case "top":
                    if (stack.isEmpty()) {
                        System.out.println(-1);
                    } else {
                        System.out.println(stack.peek());
                    }
                    break;
            }
        }
        sc.close();
    }
}