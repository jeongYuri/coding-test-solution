import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        int [][] res = new int[h][w];
        for(int i=0;i<h;i++){
            for(int j=0;j<w;j++){
                res[i][j] = -1;
            }
        }
        String[] sky = new String[h];
        for(int i=0;i<h;i++){
            sky[i] = br.readLine();
        }
        for(int i=0;i<h;i++){
            int last = -1;
            for(int j=0;j<w;j++){
                if(sky[i].charAt(j)=='c'){
                    res[i][j] = 0;
                    last = j;
                }else if(sky[i].charAt(j)=='.' &&  last!=-1){
                    res[i][j] = j-last;
                }
            }
        }
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                System.out.print(res[i][j] + " ");
            }
            System.out.println();
        }
    }
}

