import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        PriorityQueue<Integer> minHeap = new PriorityQueue<>(); //최소 힙!!!!
        int n = Integer.parseInt(br.readLine());

        for(int i=0;i<n;i++){
            int x = Integer.parseInt(br.readLine());
            if (x == 0) {
                if (minHeap.isEmpty()) {
                    sb.append("0\n");
                } else {
                    sb.append(minHeap.poll()).append("\n");
                }
            } else {
                minHeap.add(x);
            }
        }
        
        System.out.print(sb);
    }
}