import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] graph; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        Map<Character, Integer> alpha = new HashMap<>();
        alpha.put('A', 3); alpha.put('B', 2); alpha.put('C', 1); alpha.put('D', 2);
        alpha.put('E', 3); alpha.put('F', 3); alpha.put('G', 2); alpha.put('H', 3);
        alpha.put('I', 3); alpha.put('J', 2); alpha.put('K', 2); alpha.put('L', 1);
        alpha.put('M', 2); alpha.put('N', 2); alpha.put('O', 1); alpha.put('P', 2);
        alpha.put('Q', 2); alpha.put('R', 2); alpha.put('S', 1); alpha.put('T', 2);
        alpha.put('U', 1); alpha.put('V', 1); alpha.put('W', 1); alpha.put('X', 2);
        alpha.put('Y', 2); alpha.put('Z', 1);

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String a = br.readLine().trim();
        String b = br.readLine().trim();

        ArrayList<Integer> combi = new ArrayList<>();

        int len = Math.min(a.length(),b.length());
        for(int i=0;i<len;i++){
            combi.add(alpha.get(a.charAt(i)));
            combi.add(alpha.get(b.charAt(i)));
        }
        if(a.length()>b.length()){
            for(int i=0;i<a.length();i++){
                combi.add(alpha.get(a.charAt(i)));
            }
        }else if(b.length()>a.length()){
            for(int i=0;i<b.length();i++){
                combi.add(alpha.get(b.charAt(i)));
            }
        }
        while(combi.size()>2){
            ArrayList<Integer>temp = new ArrayList<>();
            for(int i=0;i<combi.size()-1;i++){
                temp.add((combi.get(i)+combi.get(i+1))%10);
            }
            combi = temp ;
        }
        System.out.print(combi.get(0));
        System.out.println(combi.get(1));
       }
}

