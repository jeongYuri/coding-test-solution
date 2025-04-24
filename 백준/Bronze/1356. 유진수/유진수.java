import java.io.*;
import java.util.*;

public class Main{
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        if(checkNumber(n)){
            System.out.println("YES");
        }else{
            System.out.println("NO");
        }
    }
    public static boolean checkNumber(int n){
        String text = Integer.toString(n);
        
        for(int i = 1;i<text.length();i++){
            String left = text.substring(0,i);
            String right = text.substring(i);

            int leftProduct = 1;
            int rightProduct = 1;

            for(int j = 0;j<left.length();j++){
                leftProduct *= left.charAt(j)-'0';
            }
            for(int j = 0;j<right.length();j++){
                rightProduct *= right.charAt(j)-'0';
            }
            if(leftProduct==rightProduct){
                return true;
            }
        }
        return false;
    }
       

    
}