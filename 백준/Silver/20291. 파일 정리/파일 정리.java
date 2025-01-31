import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

import org.xml.sax.SAXException;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        Map<String, Integer> map = new HashMap<>();

        for(int i=0;i<t;i++){
            String[] parts = br.readLine().split("\\.");
            String extension = parts[1];
            map.put(extension, map.getOrDefault(extension,0)+1);
        }
        List<String> keys = new ArrayList<>(map.keySet());
        Collections.sort(keys);

        for(String key: keys){
            System.out.println(key+" "+map.get(key));
        }
        
    }
}