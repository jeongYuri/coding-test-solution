import java.io.*;
import java.util.*;

public class Main{ 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); //수빈이랑 동생의 숨바꼭질
        int s = Integer.parseInt(st.nextToken()); //수빈이의 위치
        int maxD = 0;
        String[] inputs = br.readLine().split(" ");
        int[] locations = new int[inputs.length];
        for(int i = 0;i<inputs.length;i++){
            locations[i] = Integer.parseInt(inputs[i]);
        }
       
        for(int i = 0;i<n;i++){
            int diff = Math.abs(locations[i]-s);
            maxD = gcd(maxD,diff);
        }
        System.out.println(maxD);
        
        
    }
    public static int gcd(int a, int b){
        if(b==0) return a;
        else return gcd(b,a%b);
    }

    

}
    
