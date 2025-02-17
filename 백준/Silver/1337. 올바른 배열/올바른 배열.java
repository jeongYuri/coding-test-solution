import java.io.*;
import java.util.*;

public class Main {
    public static int check(int[] arr){
        Arrays.sort(arr);
        int n = arr.length;
        int start = 0;
        int maxCnt = 0;
        for(int end =0;end<n;end++){
            while(arr[end]-arr[start]>=5){
                start++;
            }
            int currentWindow = end-start+1;
            maxCnt = Math.max(maxCnt,currentWindow);
        }
        return Math.max(0,5-maxCnt);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int [] numbers = new int[n];
        for(int i = 0;i<n;i++){
            numbers[i] = Integer.parseInt(br.readLine());
        }
        System.out.println(check(numbers));
    }
}
