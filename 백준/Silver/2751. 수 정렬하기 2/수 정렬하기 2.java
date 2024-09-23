import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        ArrayList<Integer> nums = new ArrayList<>(n);
        
        for (int i = 0; i < n; i++) {
            nums.add(Integer.parseInt(br.readLine()));
        }
        Collections.sort(nums);
        
        for (int num : nums) {
            bw.write(Integer.toString(num));
            bw.newLine();
        }
        
        bw.flush();
        bw.close();
        br.close();
    }
}