import java.io.*;
import java.util.*;

public class Main {
    static List<List<Integer>> graph;
    static int delete;
    static int root;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] parents = new int[n];
        graph = new ArrayList<>();
        for(int i=0;i<n;i++){
            graph.add(new ArrayList<>());
        }
        for(int i=0;i<n;i++){
            parents[i] = sc.nextInt();
            if(parents[i]==-1){
                root = i; //루트 노드 설정
            }else{
                graph.get(parents[i]).add(i); //부모와 자식 관계 설정
            }
        }
        delete = sc.nextInt();
        if(delete==root){
            System.out.println(0);
        }else{
            for(List<Integer> children:graph){
                children.remove(Integer.valueOf(delete));
            }
            int res = dfs(root);
            System.out.println(res);
        }
    }
    static int dfs(int node){
        if(graph.get(node).isEmpty()){//자식 노드가 없다면
            return 1;
        }
        int leafcnt = 0;
        for(int child:graph.get(node)){
            leafcnt+= dfs(child);
        }
        return leafcnt;
    }
    }
    


