import java.io.*;
import java.util.*;

public class Main {
    static int[][] rotate45(int[][] arr, int n){
        int[][] newArr = new int[n][n];
        for(int i=0;i<n;i++){
            newArr[i] = arr[i].clone();
        }
        int mid = n/2;
        for(int i=0;i<n;i++){
            newArr[i][mid] = arr[i][i];
            newArr[i][n-1-i] = arr[i][mid];
            newArr[mid][i] = arr[n-1-i][i];
            newArr[i][i] = arr[mid][i];
        }
        return newArr;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;
        int t = Integer.parseInt(br.readLine());
        for(int tc = 0;tc<t;tc++){
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int d = Integer.parseInt(st.nextToken());

            int[][] arr = new int[n][n];
            for(int i=0;i<n;i++){
                st = new StringTokenizer(br.readLine());
                for(int j = 0;j<n;j++){
                    arr[i][j] = Integer.parseInt(st.nextToken());
                }
            }
            int rotateCnt = ((d/45)%8+8)%8; //음수 처리를 위해 +8%8
            
            for(int i = 0;i<rotateCnt;i++){
                arr = rotate45(arr,n);
            }
            
            for(int i=0;i<n;i++){
                for(int j = 0;j<n;j++){
                    bw.write(arr[i][j]+" ");
                }
                bw.write("\n");
            }
        }
        bw.flush();
        bw.close();
        bw.close();
    }
}