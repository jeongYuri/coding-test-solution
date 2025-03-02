import java.io.*;
import java.util.*;

public class Main {
    public static int cntSums(int n ){
        int[] roma = {1,5,10,50}; //사용할 수 있는 로마 숫자의 값
        Set<Integer> uniqueSum = new HashSet<>();

        getnerateCombi(roma, new int[n], 0,0, uniqueSum);
        return uniqueSum.size();
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        System.out.println(cntSums(n));
    }

    private static void getnerateCombi(int[] values, int[] combination, int idx, int start,Set<Integer> uniqueSums){
        if(idx == combination.length){
            int sum = Arrays.stream(combination).sum();
            uniqueSums.add(sum);
            return;
        }
        for(int i = start;i<values.length;i++){
            combination[idx] = values[i];
            getnerateCombi(values, combination, idx+1, i, uniqueSums);
        }

    }

}
