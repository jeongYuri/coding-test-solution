import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int l = Integer.parseInt(st.nextToken());

        int[] d = new int[n]; //신호등의 위치
        int[] r = new int[n]; //빨간불의 시간간
        int[] g = new int[n]; //초록볼의 시간

        for(int i = 0;i<n;i++){
            st = new StringTokenizer(br.readLine());
            d[i] = Integer.parseInt(st.nextToken());
            r[i] = Integer.parseInt(st.nextToken());
            g[i] = Integer.parseInt(st.nextToken());
        }

        int currentTime = 0;
        int position = 0;
        for(int i = 0;i<n;i++){
            currentTime += d[i] -position; //d[i]까지 도달하는데 걸리는 시간(1초씩 이동함)
            position = d[i];

            int cycleTime = r[i]+g[i]; //하나의 신호등 주기
            int timeInCycle = currentTime % cycleTime; //주기 내에서 현재 시간이 몇 초인지

            if(timeInCycle < r[i]){
                currentTime += (r[i]-timeInCycle);
            }
        }
        currentTime += (l - position);
        System.out.println(currentTime);
        
        }
    }

