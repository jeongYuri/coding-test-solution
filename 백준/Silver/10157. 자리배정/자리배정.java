import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int c = Integer.parseInt(st.nextToken());
        int r = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(br.readLine());

        if(k>c*r){
            System.out.println(0);
            return;
        }

        //방향 벡터(위->오->아->왼)
        int[] dx = {0,1,0,-1};
        int[] dy = {1,0,-1,0};

        boolean[][] visited = new boolean[c][r]; //좌석 방문 여부 체크
        int x = 0, y = 0,dir = 0;

        for(int i = 1;i<k;i++){
            visited[x][y] = true;
            int nx = x+dx[dir];
            int ny = y+dy[dir];
            if(nx<0 || ny<0 ||nx>=c ||ny>=r||visited[nx][ny]){
                dir = (dir+1)%4; //오른쪽 회전
                nx = x+dx[dir];
                ny = y+dy[dir];
            }
            x = nx;
            y = ny;
        }
        System.out.println((x+1)+" "+(y+1));
    }
    

        
    
   
}
