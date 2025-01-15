import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        ArrayList<ArrayList<Integer>> pascal = new ArrayList<>();
        for(int i=0;i<n;i++){
            ArrayList<Integer>row = new ArrayList<>();
            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.add(1); 
                } else {
                    
                    int value = pascal.get(i - 1).get(j - 1) + pascal.get(i - 1).get(j);
                    row.add(value);
                }
            }

            pascal.add(row);
        }

        
        System.out.println(pascal.get(n - 1).get(m - 1));
    }
}

