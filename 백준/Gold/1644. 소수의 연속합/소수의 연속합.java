import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        
        if(n==1){
            System.out.println(0);
            return;
        }

        boolean[]isPrime = new boolean[n+1];
        Arrays.fill(isPrime,true);
        isPrime[0] = isPrime[1]= false;

        for(int i = 2;i*i<=n;i++){
            if(isPrime[i]){
                for(int j = i*i;j<=n;j+=i){
                    isPrime[j] = false;
                }
            }
        }
        ArrayList<Integer> primeList = new ArrayList<>();
        for(int i = 2;i<=n;i++){
            if(isPrime[i]){
                primeList.add(i);
            }
        }
        int left  = 0,right = 0;
        int tempSum =  0;
        int cnt = 0;

        while(right<primeList.size()){
            tempSum += primeList.get(right);
            while(tempSum>n){
                tempSum -= primeList.get(left);
                left++;
            }
            if(tempSum==n){
                cnt++;
            }
            right++;
        }
        System.out.println(cnt);
        
    }     
}
    
