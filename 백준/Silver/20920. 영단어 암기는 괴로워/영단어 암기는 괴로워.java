import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;
public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        Map<String, Integer> eng = new HashMap<>();
        for(int i=0;i<n;i++){
          String word = br.readLine();
          if (word.length() >= m) {
               eng.put(word, eng.getOrDefault(word, 0) + 1);
           }
        }
        List<Map.Entry<String,Integer>> sortedList = new ArrayList<>(eng.entrySet()); //리스트로 변환후 정렬할라고~
        sortedList.sort((entry1,entry2)->{
          if(entry2.getValue()!=entry1.getValue()){
               return entry2.getValue()-entry1.getValue();
          }
          if(entry2.getKey().length()!=entry1.getKey().length()){
               return entry2.getKey().length() - entry1.getKey().length();
          }
          return entry1.getKey().compareTo(entry2.getKey());
        });
        for (Map.Entry<String, Integer> entry : sortedList) {
          bw.write(entry.getKey());
          bw.newLine();
      }

      bw.flush();
      bw.close();
    }
}
