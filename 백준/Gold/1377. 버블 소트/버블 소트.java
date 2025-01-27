import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] graph; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[][] arr = new int[n][2];

        for(int i=0;i<n;i++){
            int num = Integer.parseInt(br.readLine());
            arr[i][0] = num;
            arr[i][1] = i;
        }

        int maxN = 0;
        Arrays.sort(arr, Comparator.comparingInt(a -> a[0]));

        for(int i=0;i<n;i++){
            int diff = arr[i][1] - i;
            if(maxN<diff){
                maxN = diff;
            }
        }
        System.out.println(maxN+1);
    }
}

