import java.io.*;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        long Min = Long.parseLong(st.nextToken());
        long Max = Long.parseLong(st.nextToken());

        boolean[] check = new boolean[(int)(Max-Min+1)];
        for(long i=2;i*i<=Max;i++){
            long pow = i*i;
            long start = Min/pow;
            if(Min % pow!=0){
                start ++;
            }
            for(long j=start;j*pow<=Max;j++){
                check[(int)((j*pow)-Min)] = true;
            }
        }
        int cnt = 0;
        for(int i=0;i<=Max-Min;i++){
            if(!check[i]){
                cnt ++;
            }
        }
        System.out.println(cnt);
        
    }
}