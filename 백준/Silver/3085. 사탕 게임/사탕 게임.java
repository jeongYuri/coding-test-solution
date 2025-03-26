import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[][] candy;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        candy = new char[n][n];

        for(int i  = 0;i<n;i++){
            candy[i] = br.readLine().toCharArray();
        }
        int maxCandy = 0;

        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                if(j+1<n){
                    swap(i,j,i,j+1);
                    maxCandy = Math.max(maxCandy,cntMaxCandy());
                    swap(i,j,i,j+1);
                }
                if(i+1<n){
                    swap(i,j,i+1,j);
                    maxCandy = Math.max(maxCandy, cntMaxCandy());
                    swap(i,j,i+1,j);
                }
            }
        }
        System.out.println(maxCandy);
    }
    static void swap(int x1, int y1, int x2, int y2){
        char temp = candy[x1][y1];
        candy[x1][y1] = candy[x2][y2];
        candy[x2][y2] = temp;
    } 
    static int cntMaxCandy(){
        int maxCnt = 0;
        for(int i = 0;i<n;i++){
            int cnt = 1;
            for(int j = 1;j<n;j++){
                if(candy[i][j]==candy[i][j-1]){
                    cnt++;
                }else{
                    maxCnt = Math.max(maxCnt,cnt);
                    cnt=1;
                }
            }
            maxCnt = Math.max(maxCnt, cnt);
        }
        for(int j = 0;j<n;j++){
            int cnt = 1;
            for(int i = 1;i<n;i++){
                if(candy[i][j]==candy[i-1][j]){
                    cnt++;
                }else{
                    maxCnt = Math.max(maxCnt,cnt);
                    cnt= 1;
                }
            }
            maxCnt = Math.max(maxCnt,cnt);
        }
        return maxCnt;
    }    
}
    
