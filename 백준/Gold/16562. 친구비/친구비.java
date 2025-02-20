import java.io.*;
import java.util.*;

public class Main {
    static int[] parent;
    static int[] size;
    static int[] friendCost;

    static int find(int x){
        if(parent[x]!=x){
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    static void union(int x, int y){
        int rootX = find(x);
        int rootY = find(y);

        if(rootX!=rootY){
            if(size[rootX]<size[rootY]){
                parent[rootX] = rootY;
            }else if(size[rootX]>size[rootY]){
                parent[rootY] = rootX;
            }else{
                parent[rootY] = rootX; // 크기가 같으면 한쪽을 다른 쪽에 붙임 (보통 rootY를 rootX에 붙임)
                size[rootX]++;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken()); //학생수
        int m = Integer.parseInt(st.nextToken()); //친구 관계 수
        int k = Integer.parseInt(st.nextToken()); //가지고 있는 돈

        parent = new int[n+1];
        size = new int[n+1];
        friendCost = new int[n+1];

        String[] inputs = br.readLine().split(" ");
        for(int i = 1;i<=n;i++){
            friendCost[i]= Integer.parseInt(inputs[i-1]);
        }

        for(int i = 1;i<=n;i++){
            parent[i] = i;
            size[i] = 1;
        }

        for(int i = 0;i<m;i++){
            st = new StringTokenizer(br.readLine());
            int v = Integer.parseInt(st.nextToken());
            int w = Integer.parseInt(st.nextToken());
            union(v,w);
        }

        long totalCost = 0;
        for(int i = 1;i<=n;i++){
            if(parent[i]==i){
                int minCost = Integer.MAX_VALUE;
                for(int j = 1;j<=n;j++){
                    if(find(j)==i){
                        minCost = Math.min(minCost, friendCost[j]);
                    }
                }
                totalCost += minCost;
            }
        }

        if(totalCost<=k){
            System.out.println(totalCost);
        }else{
            System.out.println("Oh no");
        }
        
        }
    }

