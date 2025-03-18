import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            int k = Integer.parseInt(br.readLine());
            String[]texts = new String[k];
            for(int i = 0;i<k;i++){
                texts[i] = br.readLine();
            }
            String result = "0";
            for (int i = 0; i < k; i++) {
                for (int j = 0; j < k; j++) {
                    if (i != j) { 
                        String combined1 = texts[i] + texts[j]; 
                        String combined2 = texts[j] + texts[i]; 
                        
                        if (isPalindrome(combined1)) {
                            result = combined1;
                            break;
                        }
                        if (isPalindrome(combined2)) {
                            result = combined2;
                            break;
                        }
                    }
                }
                if (!result.equals("0")) break; 
            }
            
            System.out.println(result);
        }
    }

        
    public static boolean isPalindrome(String str){
        String reversed = new StringBuilder(str).reverse().toString();
        return str.equals(reversed);
    }
   
}
