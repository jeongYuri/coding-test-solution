import java.io.*;
import java.util.*;
import java.util.Comparator;
import java.util.PriorityQueue;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        int n = Integer.parseInt(br.readLine());

        PriorityQueue<int[]> pq = new PriorityQueue<>(new Comparator<int[]>() {
            public int compare(int[]a , int[] b){
                if(a[0]==b[0]){
                    return Integer.compare(a[1], b[1]);
                }
                return Integer.compare(a[0], b[0]);
            }
            
        });
        for(int i=0;i<n;i++){
            int request = Integer.parseInt(br.readLine());
            if(request==0){
                if(pq.isEmpty()){
                    bw.write("0\n");
                }else{
                    bw.write(pq.poll()[1]+"\n");
                }
            }else{
                pq.offer(new int[]{Math.abs(request),request});
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}