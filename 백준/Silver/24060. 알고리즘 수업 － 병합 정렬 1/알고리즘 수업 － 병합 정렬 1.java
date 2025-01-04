import java.io.*;
import java.util.*;
import java.util.StringTokenizer;

public class Main{
    int [] A; //입력받는 배열
    static int[] tmp; //정렬 후 저장하는 배열
    static int res = -1; //결과 저장 (실패 시 -1)
    static int cnt = 0; //저장 횟수 누적 저장
    static int k; //저장 횟수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken()); // 배열의 크기
        k = Integer.parseInt(st.nextToken()); //저장 횟수
        int[] a = new int[n];
        tmp = new int[n]; //오름차순 정렬해서 저장할 배열 초기화
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            a[i] = Integer.parseInt(st.nextToken());
        }
        merge_sort(a, 0, n-1);
        System.out.println(res);
    }
    static void merge_sort(int a[], int p, int r){
        if(cnt>k) return;
        if(p<r){
            int q = (p+r)/2; //중간으로 쪼개기~
            merge_sort(a, p, q);
            merge_sort(a, q+1, r);
            merge(a, p,q, r);
        }
    }
    static void merge(int array[], int p , int q, int r){
        int i = p;
        int j = q+1;
        int t = 0;
        while(i<=q && j<=r){
            if (array[i]<array[j]){
                tmp[t++] = array[i++];
            }else{
                tmp[t++]  = array[j++];
            }
        }
        while(i<=q){
            tmp[t++] = array[i++];

        }while(j<=r){
            tmp[t++] = array[j++];
        }
        i = p;
        t = 0;
        while(i<=r){
            cnt ++;
            if(cnt ==k){
                res = tmp[t];
                break;
            }
            array[i++] = tmp[t++];
        }
    }
}