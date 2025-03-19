import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<String> arr = new ArrayList<>();
        int[][]res = new int[n][n];

        for(int i = 0;i<n;i++){
            arr.add(br.readLine());
        }

        int[] dx = {-1,-1,-1,0,0,1,1,1};
        int[] dy = {-1,0,1,-1,1,-1,0,1};

        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                char ch = arr.get(i).charAt(j);
                if(ch!='.'){
                    res[i][j] = -1;
                    int num = Integer.parseInt(String.valueOf(ch));

                    for(int d = 0;d<8;d++){
                        int ni = i+dx[d],nj = j+dy[d];
                        if(ni>=0 && ni<n && nj>=0 && nj<n &&res[ni][nj]!=-1){
                            res[ni][nj]+= num;
                        }
                    }
                }
            }
        }
        for(int i = 0;i<n;i++){
            StringBuilder sb = new StringBuilder();
            for(int j = 0;j<n;j++){
                if (res[i][j] == -1) {
                    sb.append('*'); 
                } else if (res[i][j] >= 10) {
                    sb.append('M'); 
                } else {
                    sb.append(res[i][j]);
                }
            }
            System.out.println(sb);
            }
        }
    }
    

        
    
   

