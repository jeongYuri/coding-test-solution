import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int l = Integer.parseInt(br.readLine());
        String[] inputs = br.readLine().split(" ");
        int n = Integer.parseInt(br.readLine());

        List<Integer> s = new ArrayList<>();
        for(int i=0;i<l;i++){
            s.add(Integer.parseInt(inputs[i]));
        }
        if(s.contains(n)){
            System.out.println(0);
            return;
        }
        s.add(n);
        Collections.sort(s);
        int idx = s.indexOf(n);
        int left = (idx>0)?s.get(idx-1):0;
        int right = s.get(idx+1);
        System.out.println((n-left)*(right-n)-1);
    }
    
}

