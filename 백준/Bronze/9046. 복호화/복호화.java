import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        for(int i=0;i<t;i++){
            String[] words = br.readLine().split(" ");
            Map<Character, Integer> charCnt = new HashMap<>();
            for(String word:words){
                for(char c: word.toCharArray()){
                    charCnt.put(c,charCnt.getOrDefault(c,0)+1);
                }
            }
            int maxF = Collections.max(charCnt.values());
            List<Character> mostF = new ArrayList<>();
            for(Map.Entry<Character,Integer> entry:charCnt.entrySet()){
                if(entry.getValue()==maxF){
                    mostF.add(entry.getKey());
                }
            }
            if(mostF.size()==1){
                System.out.println(mostF.get(0));
            }else{
                System.out.println("?");
            }
        }
    }
}