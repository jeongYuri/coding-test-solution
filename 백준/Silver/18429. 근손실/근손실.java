import java.io.*;
import java.util.*;

public class Main {
    static int n, k , cnt = 0;
    static int[] kits;
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());

        kits = new int[n];
        visited = new boolean[n];
        String[] inputs = br.readLine().split(" ");

        for(int i = 0;i<n;i++){
            kits[i] = Integer.parseInt(inputs[i]);
        }
        dfs(0,500);
        System.out.println(cnt);
    }
    static void dfs(int day, int weight){
        if(day==n){
            cnt++;
            return;
        }
        for(int i = 0;i<n;i++){
            if(!visited[i]){
                int newWeight = weight + kits[i]-k;
                if(newWeight>=500){
                    visited[i] =true;
                    dfs(day+1, newWeight);
                    visited[i] = false;//백..트..래..킹
                }
            }
        }
    }
    }
