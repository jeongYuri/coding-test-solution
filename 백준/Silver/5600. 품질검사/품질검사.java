import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());
        int c = Integer.parseInt(st.nextToken());

        int total = a+b+c;
        int[] status = new int[total+1];
        Arrays.fill(status,2);// 초기 상태: "알 수 없음(2)"

        int n = Integer.parseInt(br.readLine()); //검사 횟수
        List<int[]> failedTests = new ArrayList<>();

        for(int t = 0;t<n;t++){
            st = new StringTokenizer(br.readLine());

            int i = Integer.parseInt(st.nextToken());
            int j = Integer.parseInt(st.nextToken());
            int k = Integer.parseInt(st.nextToken());
            int r = Integer.parseInt(st.nextToken());

            if(r==1){ // 검사 결과가 합격 (정상 부품 존재)
                status[i]=1;
                status[j]=1;
                status[k]=1;
            }else{// 검사 결과가 불합격 (고장 부품 존재)
                failedTests.add(new int[]{i, j, k});
            }
        }
        for(int[] test:failedTests){
            int i = test[0],j = test[1],k = test[2];
            int cnt = 0;
            int last = 1;
            if (status[i] != 1) { cnt++; last = i; }
            if (status[j] != 1) { cnt++; last = j; }
            if (status[k] != 1) { cnt++; last = k; }
            if (cnt == 1) {
                status[last] = 0;
            }
        }
        
        for(int part = 1;part<=total;part++){
            System.out.println(status[part]);



        }
    }
}
