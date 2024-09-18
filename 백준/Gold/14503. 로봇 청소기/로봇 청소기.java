import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int [][]board = new int[n][m];
        st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());
        int d = Integer.parseInt(st.nextToken());

        for (int i=0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++){
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        int cnt = 0;
        int[] dr = {-1,0,1,0};
        int[] dc = {0,1,0,-1};
        while (true) {
            if(board[r][c]==0){
                board[r][c] =2;
                cnt ++;
            }
            boolean canClean = false;
            for(int i=0; i<4;i++){
                d = (d+3)%4;
                int nr = r+dr[d];
                int nc = c+dc[d];
                if (board[nr][nc]==0){
                    r = nr;
                    c = nc;
                    canClean = true;
                    break;
                }
            }
            if(!canClean){
                int backD = (d+2)%4;
                int nr = r+dr[backD];
                int nc = c+dc[backD];
                if(board[nr][nc]==1){
                    break;
                }else{
                    r = nr;
                    c = nc;
                }
            }
        }
        System.out.println(cnt);
        
    }
}