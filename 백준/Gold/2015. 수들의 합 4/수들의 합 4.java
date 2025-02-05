import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        int[] arr = new int[n];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        long cnt = 0; //정답 수
        long prefixsum = 0; //누적합
        Map<Long,Integer>prefixcnt = new HashMap<>();
        prefixcnt.put(0L,1); //초기 값:누적합 0 이 1개 존재

        for(int num:arr){
            prefixsum+= num; //누적합 갱신
            if(prefixcnt.containsKey(prefixsum-k)){
                cnt += prefixcnt.get(prefixsum-k);
            }
            prefixcnt.put(prefixsum, prefixcnt.getOrDefault(prefixsum,0)+1);
        }
        System.out.println(cnt);
    }
}