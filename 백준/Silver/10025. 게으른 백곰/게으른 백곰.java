import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] bucket = new int[1_000_001];
        int lastIdx = 0;

        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            int g = Integer.parseInt(st.nextToken());
            int x = Integer.parseInt(st.nextToken());

            bucket[x] += g;
            lastIdx = Math.max(lastIdx,x);
        }

        int size = (2*k)+1;
        int window = 0;
        for (int i = 0; i < Math.min(size, bucket.length); i++) {
            window += bucket[i];
        }
        int ans = window;

        for(int end = size;end<=lastIdx;end++){
            window += bucket[end]; 
            window -= bucket[end - size];
            ans = Math.max(ans, window);
        }
        System.out.println(ans);
    }
}
