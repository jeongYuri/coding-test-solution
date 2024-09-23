import java.io.*;
import java.util.*;
public class Main{
    public static void main(String[] args)throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int []nums = new int[n];
        int cnt = 0;

        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            nums[i] = Integer.parseInt(st.nextToken());
        }
        for(int num:nums){
            if(isPrime(num)){
                cnt ++;
            }
        }
        System.out.println(cnt);
    }
    static boolean isPrime(int num){
        if(num<=1) return false;
        for(int i=2;i <= Math.sqrt(num);i++){
            if(num%i==0)return false;
        }
        return true;
        }
    }
