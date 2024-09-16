import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        Queue<Integer> queue = new LinkedList<>();
        int last = 0; // 마지막 요소를 추적하기 위한 변수

        int N = Integer.parseInt(br.readLine());

        for (int i = 0; i < N; i++) {
            String[] command = br.readLine().split(" ");
            
            switch (command[0]) {
                case "push":
                    last = Integer.parseInt(command[1]);
                    queue.offer(last);
                    break;
                case "pop":
                    bw.write(queue.isEmpty() ? "-1" : queue.poll().toString());
                    bw.newLine();
                    break;
                case "size":
                    bw.write(String.valueOf(queue.size()));
                    bw.newLine();
                    break;
                case "empty":
                    bw.write(queue.isEmpty() ? "1" : "0");
                    bw.newLine();
                    break;
                case "front":
                    bw.write(queue.isEmpty() ? "-1" : queue.peek().toString());
                    bw.newLine();
                    break;
                case "back":
                    bw.write(queue.isEmpty() ? "-1" : String.valueOf(last));
                    bw.newLine();
                    break;
            }
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}