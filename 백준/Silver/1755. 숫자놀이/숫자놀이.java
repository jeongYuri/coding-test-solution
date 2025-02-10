import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        ArrayList<Integer> numbers = new ArrayList<>();
        for(int t = m;t<=n;t++){
            numbers.add(t);
        }
        numbers.sort(Comparator.comparing(Main::numberToWords));

        for(int i = 0;i<numbers.size();i++){
            System.out.print(numbers.get(i)+" ");
            if((i+1)%10==0)System.out.println();
        }
        if (numbers.size() % 10 != 0) System.out.println();
    }
    public static String numberToWords(int num){
        String[] digits= {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
        StringBuilder sb = new StringBuilder();

        //숫자를 문자열로 변환 후 , 각 자리 숫자를 영어 단어로 변환
        String numStr = String.valueOf(num);
        for(int i=0;i<numStr.length();i++){
            if(i>0) sb.append(" ");
            sb.append(digits[numStr.charAt(i)-'0']);
        }
        return sb.toString();
    }  
           
}

