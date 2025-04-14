import java.io.*;
import java.util.*;

import org.xml.sax.InputSource;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        int n = Integer.parseInt(br.readLine());
        String cupholder = br.readLine();
        int couple = 0;

        for(int i = 0;i<cupholder.length()-1;i++){
            if(cupholder.charAt(i)=='L'&& cupholder.charAt(i+1)=='L'){
                couple++;
                i++;
            }
        }
        int res = n+1-couple;
        System.out.println(Math.min(n,res));






        }
}
    
