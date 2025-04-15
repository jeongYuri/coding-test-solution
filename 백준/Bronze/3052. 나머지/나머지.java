import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int [] numbers = new int[11];
        for(int i = 1;i<11;i++){
            int n = Integer.parseInt(br.readLine());
            numbers[i] = n;
        }
        List<Integer> ans = new ArrayList<>();
        for(int i =1;i<11;i++){
            int res = numbers[i]%42;
            if(!ans.contains(res)){
                ans.add(res);
            }
        }
        System.out.println(ans.size());

        
    }
}
    
