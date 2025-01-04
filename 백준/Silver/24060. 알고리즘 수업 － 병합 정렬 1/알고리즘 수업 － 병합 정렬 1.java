import java.io.*;
import java.util.*;

public class Main {
    static int[] tmp;   // 임시 배열
    static int res = -1; 
    static int cnt = 0; 
    static int k;       // 저장 횟수 기준

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        k = Integer.parseInt(st.nextToken());
        int[] arr = new int[n];
        tmp = new int[n];
        
        st = new StringTokenizer(br.readLine());
        for(int i = 0; i < n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        
        mergeSort(arr, 0, n - 1);
        System.out.println(res);
    }

    static void mergeSort(int[] arr, int left, int right){
        if(cnt >= k) return;      // k번 저장을 이미 넘어가면 종료
        if(left < right){
            int mid = (left + right) / 2;
            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }

    static void merge(int[] arr, int left, int mid, int right){
        int i = left, j = mid + 1, t = 0;
        while(i <= mid && j <= right) {
            tmp[t++] = (arr[i] < arr[j]) ? arr[i++] : arr[j++];
        }
        while(i <= mid)   tmp[t++] = arr[i++];
        while(j <= right) tmp[t++] = arr[j++];
        
        t = 0;
        for(i = left; i <= right; i++){
            cnt++;
            if(cnt == k) res = tmp[t];
            arr[i] = tmp[t++];
        }
    }
}
