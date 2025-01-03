import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;

        while((input =br.readLine())!=null){
            int n = Integer.parseInt(input.trim());
            int remainder = 1;
            int cnt =1;
            while(remainder %n!=0){
                remainder = (remainder *10+1)%n;
                cnt ++;
            }
            System.out.println(cnt);
        }
    }
}