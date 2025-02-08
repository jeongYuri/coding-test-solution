import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        
        int[][] board = new int[102][102];
        for(int t = 0;t<tc;t++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());

            for(int i = x;i<x+10;i++){
                for(int j = y;j<y+10;j++){
                    board[i][j] = 1;
                }
            }
        }
        int [][]directions = { {0, 1}, {0, -1}, {1, 0}, {-1, 0} };
        int res = 0;
        for(int i = 0;i<102;i++){
            for(int j = 0;j<102;j++){
                if(board[i][j]==1){
                    for(int[]d : directions){
                        int ni = i+d[0];
                        int nj = j+d[1];

                        if(ni<0 ||ni>=102||nj<0 ||nj>=102|| board[ni][nj]==0){
                            res+=1;
                        }
                    }
                }
            }
        }
        System.out.println(res);
    }
    
}

