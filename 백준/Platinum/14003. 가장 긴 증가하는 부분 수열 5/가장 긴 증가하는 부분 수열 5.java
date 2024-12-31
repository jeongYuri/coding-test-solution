import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n = Integer.parseInt(br.readLine());

        int[] arr = new int[n];
        int[] preIndex = new int[n];
        String[] input = br.readLine().split(" ");
        for(int i=0;i<n;i++){
            arr[i] = Integer.parseInt(input[i]);
        }
        
        ArrayList<Integer> lis = new ArrayList<>();
        lis.add(arr[0]); //첫번째 원소 추가가
        preIndex[0] = 0; //첫번째 원소의 인덱스는 0
        for(int i=1;i<n;i++){
            int key = arr[i];
            if(lis.get(lis.size()-1)<key){
                lis.add(key); //현재 원소가 lis의 마지막 원소보다 크면 추가가
                preIndex[i] = lis.size()-1;//인덱스스
            }else{
                int low = 0; //이분탐색으로 교체 위치 찾기기
                int high = lis.size()-1;
                while(low<high){
                    int mid = (low+high)/2;
                    if(lis.get(mid)>=key) high = mid;
                    else low = mid+1;
                }
                lis.set(high,key); //lis 갱신
                preIndex[i] = high; //인덱스 기록
            }
        }
        sb.append(lis.size()).append("\n");
        Stack<Integer> stack = new Stack<>();
        int index = lis.size()-1;
        for(int i = n - 1; i >= 0; i--){
            if(preIndex[i]==index){
                index--;
                stack.push(arr[i]);
            }
        }
        while(!stack.isEmpty()) sb.append(stack.pop()).append(" ");
        System.out.println(sb);
    }
    
}
