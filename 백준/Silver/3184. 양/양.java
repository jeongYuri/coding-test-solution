import java.io.*;
import java.util.*;

public class Main {
    static int r,c;
    static char[][] madang;
    static boolean[][]visited;
    static int[] dx = {0,0,-1,1};
    static int[] dy = {-1,1,0,0};
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        r = Integer.parseInt(st.nextToken());
        c = Integer.parseInt(st.nextToken());
        madang = new char[r][c];
        visited = new boolean[r][c];
        for(int i=0;i<r;i++){
           String line = br.readLine();
           for(int j=0;j<c;j++){
            madang[i][j] = line.charAt(j);
           }
        }
        int totalSheep = 0;
        int totalWolf = 0;
        for(int i=0;i<r;i++){
            for(int j=0;j<c;j++){
                if(!visited[i][j]&&madang[i][j]!='#'){
                    int[] res = bfs(i,j);
                    int sheep = res[0];
                    int wolf = res[1];
                    if(sheep>wolf){
                        totalSheep += sheep;
                    }else{
                        totalWolf += wolf;
                    }
                }
            }
        }
        System.out.println(totalSheep + " "  + totalWolf);
        
    }
    static int[] bfs(int startx, int starty){
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] {startx,starty});
        visited[startx][starty] = true;

        int sheepcnt = 0;
        int wolfcnt = 0;
        if(madang[startx][starty]=='o'){
            sheepcnt++;
        }else if(madang[startx][starty]=='v'){
            wolfcnt++;
        }
        while(!q.isEmpty()){
            int[] cur = q.poll();
            int x = cur[0];
            int y = cur[1];
            for(int i=0;i<4;i++){
                int nx = x+dx[i];
                int ny = y+dy[i];
                if(nx<0 || nx>=r || ny<0 || ny>=c){
                    continue;
                }
                if(!visited[nx][ny] && madang[nx][ny]!='#'){
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx,ny});
                    if(madang[nx][ny] =='o'){
                        sheepcnt++;
                    }else if(madang[nx][ny]=='v'){
                        wolfcnt++;
                    }
                }
            }
        }
        return new int[]{sheepcnt,wolfcnt};//양이랑 늑대 수 리턴..
    }
}
