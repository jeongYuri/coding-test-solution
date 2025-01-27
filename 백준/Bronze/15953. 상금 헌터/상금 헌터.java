import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static int[][] graph; 
    static boolean[] visited;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
        for(int i=0;i<t;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());

            int result = cal(a,b);
            System.out.println(result);
        }
    }
    public static int cal(int rank17,int rank18){
        int[]prize17 = {500,300,200,50,30,10};
        int[]count17 = {1, 2, 3, 4, 5, 6};

        int[] prize18 = {512, 256, 128, 64, 32};
        int[] count18 = {1, 2, 4, 8, 16};

        int res = 0;

        if(rank17>0){
            int position = 0;
            while(position<count17.length && rank17>count17[position]){
                rank17 -= count17[position];
                position+=1;
            }
            if(position<(prize17).length){
                res+= prize17[position];

            }
        }
        if(rank18>0){
            int position = 0;
            while(position<count18.length && rank18>count18[position]){
                rank18-= count18[position];
                position+=1;
            }
            if(position<prize18.length){
                res+= prize18[position];
            }
        }
        return res *10000;
    }
}

