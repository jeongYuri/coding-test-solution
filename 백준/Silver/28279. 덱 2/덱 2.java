import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Deque<Integer> deque = new ArrayDeque<>();
        int n = Integer.parseInt(br.readLine());
        for(int i=0;i<n;i++){
            String[] command = br.readLine().split(" ");
            int cmd = Integer.parseInt(command[0]);
            switch (cmd) {
                case 1:
                    int x1 = Integer.parseInt(command[1]);
                    deque.addFirst(x1);
                    break;
                case 2:
                    int x2 = Integer.parseInt(command[1]);
                    deque.addLast(x2);
                    break;
                case 3:
                    System.out.println(deque.isEmpty() ? -1 : deque.pollFirst());
                    break;
                case 4:
                    System.out.println(deque.isEmpty() ? -1 : deque.pollLast());
                    break;
                    
                case 5:
                    System.out.println(deque.size());
                    break;
                case 6:
                    System.out.println(deque.isEmpty() ? 1 : 0);
                    break;
                case 7:
                    System.out.println(deque.isEmpty() ? -1 : deque.peekFirst());
                    break;
                case 8:
                    System.out.println(deque.isEmpty() ? -1 : deque.peekLast());
                    break;
                default:
                    break;
            }
        }
    }
    
}
