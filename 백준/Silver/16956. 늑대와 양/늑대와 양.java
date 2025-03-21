import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int r = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        char[][] farm = new char[r][c];
        boolean flag = true;
        for (int i = 0; i < r; i++) {
            String line = br.readLine();
            for(int j = 0;j<c;j++){
                farm[i][j] = line.charAt(j);
            }
        }

        int[] dx = {0,0,1,-1};  // 상하좌우
        int[] dy = {1,-1,0,0};

        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (farm[i][j] == 'W') {  
                    for (int d = 0; d < 4; d++) {
                        int ni = i + dx[d];
                        int nj = j + dy[d];
                        if (ni >= 0 && ni < r && nj >= 0 && nj < c) {
                            if (farm[ni][nj] == 'S') {  // 늑대가 근처에 있으면 불가능
                                flag = false;
                                System.out.println(0);
                                return;
                            }else if(farm[ni][nj]=='.'){
                                farm[ni][nj] = 'D';
                            }
                        }
                    }
                }
            }
        }
        if(!flag){
            System.out.println(0);
        }else{
            StringBuilder sb = new StringBuilder();
            System.out.println(1);
            for(int i = 0;i<r;i++){
                sb.append(farm[i]);
                sb.append("\n");
            }
            System.out.println(sb);
        }
    }
}