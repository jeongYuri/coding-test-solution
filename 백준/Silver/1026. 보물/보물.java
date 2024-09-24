import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int []a = new int[n];
        Integer[] b = new Integer[n];
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a);
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            b[i] = Integer.parseInt(st.nextToken()); 
        }

        Arrays.sort(b, Comparator.reverseOrder());
        int s =0;
        for(int i=0;i<n;i++){
            s += a[i]*b[i];
        }
        System.out.println(s);
    }
}