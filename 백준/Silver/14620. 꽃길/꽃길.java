import java.io.*;
import java.util.*;

public class Main{
	static int n;
	static int[][] map;
	static boolean[][] visited;
	static int[] dx = {-1,1,0,0};
	static int[] dy = {0,0,-1,1};
	static int cost = Integer.MAX_VALUE;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		n = Integer.parseInt(br.readLine());
		map = new int[n][n];
		visited = new boolean[n][n];

		for(int i = 0;i<n;i++){
			StringTokenizer st = new StringTokenizer(br.readLine());
			for(int j = 0;j<n;j++){
				map[i][j] = Integer.parseInt(st.nextToken());

			}
		}
		dfs(0,0);
		System.out.println(cost);
	}
	static void dfs(int cnt, int total){
		if(cnt==3){
			cost = Math.min(cost, total);
			return ;
		}
		for(int i =1;i<n-1;i++){
			for(int j = 1;j<n-1;j++){
				if(check(i,j)){
					int costs = plant(i,j,true);
					dfs(cnt+1, total+costs);
					plant(i,j,false);
				}
			}
		}
	}
	static boolean check(int x, int y){
		if(visited[x][y]) return false;
		for(int i = 0;i<4;i++){
			int nx = x+dx[i];
			int ny = y+dy[i];
			if(nx<0||ny<0|| nx>=n || ny>=n || visited[nx][ny]){
				return false;	
			}

		}
		return true;
	}
    static int plant(int x, int y ,boolean flag){
		int sum = map[x][y];
		visited[x][y] = flag;

		for(int i = 0;i<4;i++){
			int nx = x+dx[i];
			int ny = y+dy[i];
			visited[nx][ny] = flag;
			sum+= map[nx][ny];
		}
		return flag? sum:0;
	} 

    
}