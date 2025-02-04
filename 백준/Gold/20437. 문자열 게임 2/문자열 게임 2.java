import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        while(t-->0){
            String w = br.readLine().trim();
            int k = Integer.parseInt(br.readLine());

            Map<Character,Integer> cntMap = new HashMap<>();
            Map<Character, List<Integer>> indexMap = new HashMap<>();

            for(int i=0;i<w.length();i++){
                char c= w.charAt(i);
                cntMap.put(c,cntMap.getOrDefault(c,0)+1);
                if(!indexMap.containsKey(c)){
                    indexMap.put(c, new ArrayList<>());
                }
                indexMap.get(c).add(i);
            }
            boolean check = false;
            int minAns = Integer.MAX_VALUE;
            int maxAns = -1;

            for(char key:indexMap.keySet()){
                if(cntMap.get(key)<k)continue;
                check = true;
                List<Integer> indexs = indexMap.get(key);
                for(int i=0;i<=indexs.size()-k;i++){
                    int length = indexs.get(i+k-1)-indexs.get(i)+1;
                    minAns = Math.min(minAns,length);
                    maxAns = Math.max(maxAns,length);
                }
            }
            if(check){
                System.out.println(minAns+" "+maxAns);
            }else{
                System.out.println(-1);
            }
        }
    }
}