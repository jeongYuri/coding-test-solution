import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        String[] room = new String[n];
        for(int i = 0;i<n;i++){
            room[i] = br.readLine();
        }
        int cnt = 0;
        for(int i=0;i<n;i++){
            char temp = ' ';
            for(int j = 0;j<m;j++){
                if (room[i].charAt(j) == '-' && room[i].charAt(j) != temp){
                    cnt +=1;
                }
                temp = room[i].charAt(j);
            }
        }
        for(int j = 0;j<m;j++){
            char temp =' ';
            for(int i = 0;i<n;i++){
                if(room[i].charAt(j)=='|' && room[i].charAt(j)!=temp){
                    cnt ++;
                }
                temp = room[i].charAt(j);
            }
        }
        System.out.println(cnt);
    }
}
