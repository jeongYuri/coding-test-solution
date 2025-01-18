import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.HashSet;
import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.Scanner;
import java.util.Set;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args)throws IOException {
       BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       StringTokenizer st = new StringTokenizer(br.readLine());
       int n = Integer.parseInt(st.nextToken());
       String game = st.nextToken();
       Set<String> players = new HashSet<>();
       for(int i=0;i<n;i++){
         String name = br.readLine();
         players.add(name);
       }
       int p = players.size();
       if(game.equals("Y")){
        System.out.println(p);
       }else if(game.equals("F")){
        System.out.println(p/2);
       }else{
        System.out.println(p/3);
       }
    }

    
}