import java.util.*;
import java.io.*;

public class Main{
    static char[] res;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int [] arr = new int[n];
        String[] input = br.readLine().split(" ");
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(input[i]);
        }
        if (prevPermutation(arr)) {
            System.out.println(Arrays.toString(arr).replaceAll("[\\[\\],]", ""));
        } else {
            System.out.println("-1");
        }
    }
    private static boolean prevPermutation(int[] arr){
        int i = arr.length-1;
        while(i>0 && arr[i-1]<=arr[i]){
            i--;
        }
        if(i==0){
            return false;
        }
        int j = arr.length -1;
        while(arr[j]>=arr[i-1]){
            j--;
        }
        swap(arr, i - 1, j);
        reverse(arr, i, arr.length-1);
        return true;

    }
    private static void swap(int[] arr, int a, int b){
        int temp = arr[a];
        arr[a] = arr[b];
        arr[b] = temp;
    }
    private static void reverse(int[]arr, int start, int end){
        while(start<end){
            swap(arr, start, end);
            start++;
            end--;
        }
    }
    }
