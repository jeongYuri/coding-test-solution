import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		int [][]dist = new int[n][m];
		int[][] sea = new int[n][m];

		for(int i = 0;i<n;i++){
			String[]inputs = br.readLine().split(" ");
			
			for(int k = 0;k<m;k++){
				sea[i][k] = Integer.parseInt(inputs[k]) ;
				dist[i][k]  = -1;
				}
			}
		

		int [][] dir = {{-1,-1},{-1,0},{-1,1},{0,-1},{0,1},{1,-1},{1,0},{1,1}};
		Queue<int[]> q = new LinkedList<>();

		for(int i = 0;i<n;i++){
			for(int j = 0;j<m;j++){
				if(sea[i][j]==1){
					q.add(new int[]{i,j});
					dist[i][j] = 0;
				}
			}
		}

		while(!q.isEmpty()){
			int[] cur = q.poll();
			for(int[] d:dir){
				int ni = cur[0]+d[0];
				int nj = cur[1]+d[1];
				if(ni>=0 && nj>=0 && ni<n && nj<m && dist[ni][nj]==-1){
					dist[ni][nj] = dist[cur[0]][cur[1]]+1;
					q.add(new int[]{ni,nj});
				}
			}
		}
		int max = 0;
		for(int i = 0;i<n;i++){
			for(int j = 0;j<m;j++){
				max = Math.max(max, dist[i][j]);
			}
		}
		System.out.println(max);

	} 
	   
}