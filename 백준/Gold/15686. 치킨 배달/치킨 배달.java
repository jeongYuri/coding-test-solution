import java.io.*;
import java.util.*;

public class Main {
    static int n,m;
    static List<int[]> home = new ArrayList<>();
    static List<int[]> chick = new ArrayList<>();
    static int res = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
  
        for(int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++){
                int value = Integer.parseInt(st.nextToken());
                if(value ==1){
                    home.add(new int[]{i,j});
                }else if(value ==2){
                    chick.add(new int[]{i,j});
                }
            } 
        }
        combination(new ArrayList<>(),0);
        System.out.println(res);    
    }
    public static void combination(List<int[]> selected, int start){
        if(selected.size()==m){
            int total = 0;
            for(int[] h:home){
                int minDistance = Integer.MAX_VALUE;
                for(int[] c: selected){
                    int distance = Math.abs(h[0]-c[0])+Math.abs(h[1]-c[1]);
                    minDistance = Math.min(minDistance,distance);
                }
                total += minDistance;
            }
            res = Math.min(res, total);
            return;
        }
        for(int i=start;i<chick.size();i++){
            selected.add(chick.get(i));
            combination(selected, i+1);
            selected.remove(selected.size()-1);
        }
    }
}