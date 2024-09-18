import java.io.*;
import java.util.*;

public class Main{
    static int[] dx = {-1,0,1,0};
    static int[] dy = {0,-1,0,1};
    static int n;
    static int[][] sea;
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        sea = new int[n][n];
        int sharkx = 0, sharky = 0;
        for(int i=0; i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            for(int j=0;j<n;j++){
                sea[i][j] = Integer.parseInt(st.nextToken());
                if(sea[i][j]==9){
                    sharkx = i;
                    sharky = j;
                    sea[i][j] = 0;//아기상어 있던 자리
                }
            }
        }
        int sharsize = 2;
        int eaten = 0;
        int time =0;
        while(true){
            boolean [][] visited = new boolean[n][n];
            Queue<int[]> q = new LinkedList<>();
            PriorityQueue<int []>fishes = new PriorityQueue<>((a,b)->{
                if(a[2]!=b[2]) return a[2]-b[2];//거리
                if(a[0]!=b[0]) return a[0]-b[0];//x좌표 비교
                return a[1]-b[1];
            });
            q.offer(new int[]{sharkx,sharky,0});
            visited[sharkx][sharky] = true;
            while(!q.isEmpty()){
                int[]current = q.poll();
                int x = current[0],y = current[1],dist = current[2];
                for (int i=0;i<4;i++){
                    int nx = x+dx[i];
                    int ny = y+dy[i];
                    if(nx<0 || nx>=n ||ny<0||ny>=n||visited[nx][ny]) continue;
                    if (sea[nx][ny]>sharsize)continue;
                    visited[nx][ny] = true;
                    q.offer(new int[]{nx,ny,dist+1});
                    if(sea[nx][ny]>0 && sea[nx][ny]<sharsize){
                        fishes.offer(new int[]{nx,ny,dist+1});
                    }
                }
            }
            if (fishes.isEmpty())break; //no 물고기
            int[] fish = fishes.poll();
            int fishx = fish[0],fishy = fish[1],fishdist = fish[2];
            time += fishdist;
            eaten ++;
            if(eaten == sharsize){
                sharsize++;
                eaten = 0;
            }
            sea[fishx][fishy] = 0;
            sharkx = fishx;
            sharky = fishy;
        } 
        System.out.println(time);
    }
}