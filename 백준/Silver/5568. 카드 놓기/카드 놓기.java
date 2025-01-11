import java.io.*;
import java.util.*;

public class Main {
    static int n,k;
    static String[] cards;
    static boolean[] used;
    static Set<String> combs = new HashSet<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());

        cards = new String[n];
        for(int i=0;i<n;i++){
            cards[i] = br.readLine().trim();
        }
        used = new boolean[n];
        backtrack(0,"");
        System.out.println(combs.size());
    }
    private static void backtrack(int depth, String current){
        if(depth==k){
            combs.add(current);
            return;
        }
        for(int i=0;i<n;i++){
            if(!used[i]){
                used[i] = true;
                backtrack(depth+1, current+cards[i]);
                used[i] = false;
            }
        }
    }
    }
    


