import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String [] line = br.readLine().split(" ");
        int[] numbers  = new int[n];
        for(int i = 0;i<n;i++){
            numbers[i] = Integer.parseInt(line[i]);
        }
        List<Integer> res = new ArrayList<>();
        int cnt = 0;
        for(int i = 0;i<n-1;i++){
            if(numbers[i]<numbers[i+1]){
                cnt += numbers[i+1]-numbers[i];
            }else if(numbers[i]>numbers[i+1] || numbers[i]==numbers[i+1]){
                res.add(cnt);
                cnt = 0;
            }
        }
        if(cnt>0) res.add(cnt);

        if(res.size()>0){
            int ans = Collections.max(res);
            System.out.println(ans);
        }else{
            System.out.println(0);
        }
        
    }
}
    
