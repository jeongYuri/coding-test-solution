import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[][] cookie;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        cookie = new char[n][n];

        for(int i =0;i<n;i++){
            String line = br.readLine();
            for(int j = 0;j<n;j++){
                cookie[i][j] = line.charAt(j); 
            }
        }
        //머리 위치 찾기
        int[] head = findHead();
        int hy = head[0];
        int hx = head[1];

        int heartY = hy+1;
        int heartX = hx;
        System.out.println((heartY+1)+" "+ (heartX+1));

        int leftArm = countLeft(heartY,heartX);
        int rightArm = countRight(heartY, heartX);
        int waist = countWaist(heartY+1, heartX);
        int leftLeg = countLeg(heartY+waist+1, heartX-1);
        int rightLeg = countLeg(heartY+waist+1, heartX+1);

        System.out.println(leftArm+" "+rightArm+" "+waist+" "+ leftLeg+" "+rightLeg);
    }
    static int[] findHead(){
        for(int i = 0;i<n;i++){
            for(int j = 0;j<n;j++){
                if(cookie[i][j]=='*'){
                    return new int[]{i,j};
                }
            }
        }
        return new int[]{-1,-1};
    }
    static int countLeft(int y , int x){
        int cnt = 0;
        for(int i = x-1;i>=0;i--){
            if(cookie[y][i]=='_') break;
            cnt++;
        }
        return cnt;
    }
    static int countRight(int y, int x){
        int cnt = 0;
        for(int i=x+1;i<n;i++){
            if(cookie[y][i]=='_')break;
            cnt++;
        }
        return cnt;
    }
    static int countWaist(int y, int x){
        int cnt = 0;
        for(int i = y;i<n;i++){
            if(cookie[i][x]=='_')break;
            cnt ++;
        }
        return cnt;
    }
    static int countLeg(int y, int x){
        int cnt = 0;
        for(int i = y;i<n;i++){
            if(cookie[i][x]=='_')break;
            cnt++;
        }
        return cnt;
    }
}
