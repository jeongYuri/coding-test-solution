import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<int[]> storage = new ArrayList<>();

        for(int i = 0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            int h = Integer.parseInt(st.nextToken());

            storage.add(new int[]{l,h});
         }

         storage.sort(Comparator.comparingInt(a->a[0]));
         int left = storage.get(0)[0];
         int right = 0;
         for(int[] s: storage){
            right = Math.max(right, s[0]);
         }

        int[] leftMax = new int[right+2]; //왼쪽에서 오른쪽으로
        leftMax[storage.get(0)[0]] = storage.get(0)[1];

        int idx = storage.get(0)[0];
        leftMax[idx] = storage.get(0)[1];
        for (int i = idx + 1; i <= right; i++) {
            leftMax[i] = leftMax[i-1];
            for (int[] s : storage) {
                if (s[0] == i) {
                    leftMax[i] = Math.max(leftMax[i], s[1]);
                }
            }
        }

        int[] rightMax = new int[right+2];
        idx = storage.get(storage.size() - 1)[0];
        rightMax[idx] = storage.get(storage.size() - 1)[1];
        for (int i = idx - 1; i >= left; i--) {
            rightMax[i] = rightMax[i+1];
            for (int[] s : storage) {
                if (s[0] == i) {
                    rightMax[i] = Math.max(rightMax[i], s[1]);
                }
            }
        }

        int total = 0;
        for(int i = 0;i<=right;i++){
            total+= Math.min(leftMax[i],rightMax[i]);
        }

        System.out.println(total);
    }
}
    
