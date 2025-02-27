import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());

        StringBuilder sb = new StringBuilder();
        for(int i = 0;i<n;i++){
            String[] input = br.readLine().split(" ");
            int first = Integer.parseInt(input[0]);

            if(first==0){
                if(heap.isEmpty()){
                    sb.append("-1\n");
                }else{
                    sb.append(heap.poll()).append("\n");
                }
            }else{
                for(int j = 1;j<input.length;j++){
                    heap.offer(Integer.parseInt(input[j]));
                }
            }
        }
        System.out.println(sb.toString());
    }
    }
