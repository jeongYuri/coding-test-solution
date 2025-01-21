import java.io.*;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> cards = new PriorityQueue<>();
        for(int i=0;i<n;i++){
            cards.offer(Integer.parseInt(br.readLine()));
        }
        int total = 0;
        while(cards.size()>1){
            int hab = cards.poll()+cards.poll();
            total+=hab;
            cards.offer(hab);
        }
        System.out.println(total);

    }
}