import java.util.*;
import java.io.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        List<int[]> permutations = generatePermutations(); //순열 생성성
        for(int i=0;i<n;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int num = Integer.parseInt(st.nextToken());
            int s = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            List<int[]> tmp = new ArrayList<>();
            for(int[] candidate:permutations){
                int[] result = count(candidate,num);
                int strike = result[0];
                int ball = result[1];
                if(strike == s && ball == b){
                    tmp.add(candidate);
                }
            }
            permutations = tmp;//후보 리스트 업데이트
        }
        System.out.println(permutations.size());

    }
    private static List<int[]> generatePermutations(){
        List<int[]> permutations = new ArrayList<>();
        for(int i=1;i<=9;i++){
            for(int j=1;j<=9;j++){
                if(i==j) continue;
                for(int k=1;k<=9;k++){
                    if(k==i || k==j)continue;
                    permutations.add(new int[]{i,j,k});
                }
            }
        }
        return permutations;
    }
    private static int[] count(int[] candidate,int num){
        int strike = 0, ball = 0;
        String numStr = String.valueOf(num);
        for(int i=0;i<3;i++){
            int digit= numStr.charAt(i)-'0';
            if(candidate[i]==digit){
                strike++;
            }else if(contains(candidate,digit)){
                ball++;
            }
        }
        return new int[]{strike,ball};
    }
    private static boolean contains(int[] array, int value){
        for(int num:array){
            if(num==value) return true;
        }
        return false;
    }
}