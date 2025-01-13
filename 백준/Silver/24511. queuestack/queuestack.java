import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());    
        st = new StringTokenizer(br.readLine(), " ");
        int[] a = new int[n];
        for(int i = 0; i < n; i++){
            a[i] = Integer.parseInt(st.nextToken());
        }

        st = new StringTokenizer(br.readLine(), " ");
        int[] b = new int[n];
        for(int i = 0; i < n; i++){
            b[i] = Integer.parseInt(st.nextToken());
        }

        int m = Integer.parseInt(br.readLine());
        st = new StringTokenizer(br.readLine(), " ");
        int[] c = new int[m];
        for(int j = 0; j < m; j++){
            c[j] = Integer.parseInt(st.nextToken());
        }

        Deque<Integer> qs = new ArrayDeque<>();
        for(int i = 0; i < n; i++){
            if(a[i] == 0){
                qs.addLast(b[i]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for(int x : c){
            qs.addFirst(x);
            int out = qs.removeLast();
            sb.append(out).append(' ');
        }
        System.out.println(sb.toString().trim());
    }
}
