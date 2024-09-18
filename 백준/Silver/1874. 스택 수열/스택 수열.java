import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(br.readLine());
        Stack<Integer> stack = new Stack<>();
        int current = 1;

        for(int i=0;i<n;i++){
            int num = Integer.parseInt(br.readLine());
            while(current<= num){
                stack.push(current);
                sb.append("+\n");
                current++;
            }
            if (!stack.isEmpty() && stack.peek() == num) {
                stack.pop();
                sb.append("-\n");
            } else {
                System.out.println("NO");
                return;
            }
        }
        System.out.print(sb);
    }
}