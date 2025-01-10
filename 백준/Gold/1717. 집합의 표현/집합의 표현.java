import java.io.*;
import java.util.*;

public class Main {
    static int find(int[] parents,int x){
        if(parents[x]!=x){
            parents[x] = find(parents,parents[x]);
        }return parents[x];
    }
    static void union(int[] parents,int[] rank, int a, int b){
        int rootA = find(parents, a);
        int rootB = find(parents, b);
        if(rootA !=rootB){
            if(rank[rootA]<rank[rootB]){
                parents[rootA] = rootB;
            }else if(rank[rootA]>rank[rootB]){
                parents[rootB]=rootA;
            }else{
                parents[rootB] = rootA;
                rank[rootA]++;
            }
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();

        String[] nm  = br.readLine().split(" ");
        int n = Integer.parseInt(nm[0]);
        int m = Integer.parseInt(nm[1]);

        int[] parents = new int[n+1];
        int[] rank = new int[n+1];
        for(int i=0;i<=n;i++){
            parents[i] = i;
            rank[i] = 0;
        }
        for(int i=0;i<m;i++){
            String[] input = br.readLine().split(" ");
            int op = Integer.parseInt(input[0]);
            int a = Integer.parseInt(input[1]);
            int b = Integer.parseInt(input[2]);
            if(op==0){
                union(parents, rank, a, b);
            }else if(op==1){
                if(find(parents,a)==find(parents, b)){
                    sb.append("YES\n");
                }else{
                    sb.append("NO\n");
                }
            }
        }
        System.out.print(sb);
    }
    }
    


