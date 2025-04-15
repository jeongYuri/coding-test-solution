import java.io.*;
import java.util.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        int[] numbers = new int[45];
        for(int i = 0;i<45;i++){//삼각수..
            numbers[i] = i*(i+1)/2; //t = n(n+1)/2를 나타낸 것..!
        }
        for(int i = 0;i<tc;i++){
            int k = Integer.parseInt(br.readLine());
            int res = result(k,numbers);
            System.out.println(res);
        }

    }
    public static int result(int n, int[] triNum){
        for(int j = 1;j<45;j++){
            for(int k = 1;k<45;k++){
                for(int z = 1;z<45;z++){
                    int sum = triNum[j]+triNum[k]+triNum[z];
                    if(sum==n){
                        return 1;
                    }
                }
            }
        }
        return 0;
    }
}
    
