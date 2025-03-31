import java.io.*;
import java.util.*;

public class Main {
    static int[][]board = new int[5][5];
    static HashSet<String> uoniqueNumber = new HashSet<>();
    static int[] dx = {-1,1,0,0};
    static int[] dy = {0,0,-1,1};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        for(int i = 0;i<5;i++){
            String[] inputs = br.readLine().split(" ");
            for(int j = 0;j<5;j++){
                board[i][j] = Integer.parseInt(inputs[j]);
            }
        }
        for(int i = 0;i<5;i++){
            for(int j = 0;j<5;j++){
                dfs(i,j,"",0);
            }
        }
        System.out.println(uoniqueNumber.size());
    }
    static void dfs(int x, int y, String num, int depth){
        if(depth==6){
            uoniqueNumber.add(num);
            return;
        }
        for(int i = 0;i<4;i++){
            int nx = x+dx[i];
            int ny = y+dy[i];

            if(nx>=0 && nx<5&& ny>=0 && ny<5){
                dfs(nx,ny,num+board[nx][ny],depth+1);
            }
        }
    }
    
}
    
