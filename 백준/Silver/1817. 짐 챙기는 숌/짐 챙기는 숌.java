import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m  = Integer.parseInt(st.nextToken());
        if(n==0){
            System.out.println(0);
            return;
        }
        st = new StringTokenizer(br.readLine());
        int[] books = new int[n];
        for(int i=0;i<n;i++){
            books[i] = Integer.parseInt(st.nextToken());
        }
        int temp = 0;
        int res = 0;
        for(int i=0;i<n;i++){
            if(temp+books[i]>m){
                res++;
                temp = books[i];
            }else{
                temp += books[i];
            }
        }
        if(temp>0){
            res++;
        }
        System.out.println(res);

        
            }
        }
    