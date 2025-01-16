import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] input = br.readLine().split(" ");
        Integer[] tree = new Integer[n];
        for(int i=0;i<n;i++){
            tree[i] = Integer.parseInt(input[i]);
        }
        Arrays.sort(tree, Collections.reverseOrder());
        int day = 0;
        for(int i=0;i<n;i++){
            day = Math.max(day, tree[i]+i+1);
        }
        System.out.println(day+1);
        }
    }


