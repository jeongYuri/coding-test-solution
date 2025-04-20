import java.io.*;
import java.util.*;

public class Main{
    static int min = Integer.MAX_VALUE;
    static int num;
       public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        num = Integer.parseInt(br.readLine()); 

        List<Integer> arrList = new ArrayList<>();
        for(char c:String.valueOf(num).toCharArray()){
            arrList.add(Character.getNumericValue(c));
        }

        int n = arrList.size();
        int[] arr = new int[n];
        boolean[] visited = new boolean[n];
        List<Integer> temp = new ArrayList<>();
        
        for(int i = 0;i<n;i++){
            arr[i] = arrList.get(i);
        }
        
        permutation(arr, visited,temp,n);
        
        if (min == Integer.MAX_VALUE) {
            System.out.print(0); // 못 찾으면 0 출력
        } else {
            System.out.print(min);
        }
        
    }

    static void permutation(int[] arr, boolean[]visited,List<Integer> temp, int n){
        if(temp.size()==n){
            StringBuilder sb = new StringBuilder();
            for(int num:temp){
                sb.append(num);
            }
            int val = Integer.parseInt(sb.toString());
            if (val > num) { 
                min = Math.min(min, val);
            }
            return;
    }
    for(int i =0;i<n;i++){
        if(!visited[i]){
            visited[i] = true;
            temp.add(arr[i]);
            permutation(arr, visited, temp, n);
            temp.remove(temp.size()-1);
            visited[i] = false;
        }
    }
        
        
    
    
    }

}
    
