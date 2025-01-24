import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] graph; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       while(true){
            String[] input = br.readLine().split(" ");
            int n = Integer.parseInt(input[0]);
            int m = Integer.parseInt(input[1]);

            if(n==0 && m==0){
                break;
            }
            List<Integer> sang = new ArrayList<>();
            List<Integer> sun  = new ArrayList<>();

            for(int i=0;i<n;i++){
                sang.add(Integer.parseInt(br.readLine()));
            }
            for(int i=0;i<m;i++){
                sun.add(Integer.parseInt(br.readLine()));
            }
            int idxN = 0, idxM = 0;
            int cnt = 0;

            while(idxN< n && idxM<m){
                int sangCD = sang.get(idxN);
                int sunCD = sun.get(idxM);

                if(sangCD == sunCD){
                    cnt++;
                    idxM++;
                    idxN++;
                }else if(sangCD<sunCD){
                    idxN++;
                }else{
                    idxM++;
                }
            }
            System.out.println(cnt);
       }
}
}
