import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;

        int n = Integer.parseInt(br.readLine());    
        int target = Integer.parseInt(br.readLine());
        int[][] snail = new int[n][n];
        int[] dr = {1,0,-1,0};
        int[] dc = {0,1,0,-1};
        int r = 0, c=0;
        int direction = 0;
        int num = n*n;

        snail[r][c] = num;
        num--;

        while(num>0){
            int nr = r+dr[direction];
            int nc = c+dc[direction];

            if(nr<0 || nr>=n || nc<0 || nc>=n || snail[nr][nc]!=0){
                direction = (direction+1)%4;
                nr = r+dr[direction];
                nc = c+dc[direction];
            }
            snail[nr][nc] = num;
            num--;
            r = nr;
            c = nc;
        }
        int pos_r = 0, pos_c = 0;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(snail[i][j]== target){
                    pos_r = i+1;
                    pos_c = j+1;
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                sb.append(snail[i][j]).append(" ");
            }
            sb.append("\n");
        }
        sb.append(pos_r).append(" ").append(pos_c);
        System.out.print(sb.toString());
    }
}
