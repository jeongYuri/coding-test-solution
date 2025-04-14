import java.io.*;
import java.util.*;

import org.xml.sax.InputSource;

public class Main {
    static ArrayList<Integer>[] graph;
    static int[] visited;
    static int cnt = 1; 
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        int rowCnt = 0;
        int colCnt = 0;
        List<String> castle = new LinkedList<>();
        for(int i = 0;i<n;i++){
            String input = br.readLine();
            castle.add(input);
        }
        for(int i = 0;i<n;i++){
            String line = castle.get(i);
            if(!line.contains("X")){
                rowCnt++;
            }
        }
        for(int j = 0;j<m;j++){
            boolean hasX = false;
            for(int i = 0;i<n;i++){
                if(castle.get(i).charAt(j)=='X'){
                    hasX = true;
                    break;
                }
            }
            if(!hasX){
                colCnt++;
            }
        }
        System.out.println(Math.max(rowCnt, colCnt));
        }


        
    
    
}
    
