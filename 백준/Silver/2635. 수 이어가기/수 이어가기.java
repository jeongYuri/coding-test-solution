import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> res = new ArrayList<>();

        for (int i = 1; i <= n; i++) {
            ArrayList<Integer> tmp = new ArrayList<>();
            tmp.add(n); 
            tmp.add(i); 
  
            while (tmp.get(tmp.size() - 1) >= 0) {
                int size = tmp.size();
                tmp.add(tmp.get(size - 2) - tmp.get(size - 1));
            }
            tmp.remove(tmp.size() - 1); 

            if (tmp.size() > res.size()) {
                res = new ArrayList<>(tmp);
            }
        }
        System.out.println(res.size());
        for (int num : res) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}