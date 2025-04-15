import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        for(int i = 0;i<tc;i++){

            String line = br.readLine();
            int hab = 0;
            int score = 0;
            for(int j = 0;j<line.length();j++){
                if(line.charAt(j)=='O'){
                        score++;
                        hab+= score;
                }else{
                    score = 0;
                }
            }
            System.out.println(hab);
        }
        
    }
}
    
