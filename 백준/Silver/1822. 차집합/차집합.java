import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        st = new StringTokenizer(br.readLine());
        Set<Integer> ac = new HashSet<>();
        for(int i=0;i<a;i++){
            ac.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(br.readLine());
        Set<Integer>bc = new HashSet<>();
        for(int i=0;i<b;i++){
            bc.add(Integer.parseInt(st.nextToken()));
        }
        ac.removeAll(bc);
        System.out.println(ac.size());
        List<Integer> res = new ArrayList<>(ac);
        Collections.sort(res);
        for (int num : res) {
            System.out.print(num + " ");
        }
        }
        }
    


