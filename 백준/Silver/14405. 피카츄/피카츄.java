import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args)throws IOException {
       Scanner sc = new Scanner(System.in);
       String s = sc.nextLine().trim();
       String[] pikachu = {"pi","ka","chu"};
       for(String p:pikachu){
        s = s.replace(p, " ");
       }
       if(s.trim().isEmpty()){
        System.out.println("YES");
       }else{
        System.out.println("NO");
       }

    }

    
}