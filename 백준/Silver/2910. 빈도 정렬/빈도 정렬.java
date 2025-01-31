import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        String[] inputs = br.readLine().split(" ");
        List<Integer>message = new ArrayList<>();
        Map<Integer,Integer> freq =  new HashMap<>();
        Map<Integer,Integer> first = new LinkedHashMap<>();

        for(int i=0;i<n;i++){
            int num = Integer.parseInt(inputs[i]);
            message.add(num);
            freq.put(num,freq.getOrDefault(num,0)+1);
            first.putIfAbsent(num,i);
        }
        message.sort((a,b)->{
            int freqcompare = freq.get(b)-freq.get(a);
            if(freqcompare==0){
                return first.get(a)-first.get(b);
            }
            return freqcompare;

        });

        for(int num:message){
            System.out.print(num+" ");
        }
        
        
    
    }
}