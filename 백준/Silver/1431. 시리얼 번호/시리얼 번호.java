import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;
public class Main {
    public static int sumOfDigits(String s){
      int sum = 0;
      for(char ch:s.toCharArray()){
        if(Character.isDigit(ch)){
          sum+= ch-'0';
        }
      }
      return sum;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
       
        int n = Integer.parseInt(br.readLine());
        ArrayList<String> arr = new ArrayList<>();
        for(int i=0;i<n;i++){
          arr.add(br.readLine().trim());
        }
        Collections.sort(arr,new Comparator<String>() {
          @Override
          public int compare(String s1, String s2){
            if(s1.length()!=s2.length()){
              return Integer.compare(s1.length(),s2.length());
            }
            int sum1 = sumOfDigits(s1);
            int sum2 = sumOfDigits(s2);
            if(sum1!=sum2){
              return Integer.compare(sum1, sum2);
            }
            return s1.compareTo(s2);
          }
        });
        for(String str:arr){
          System.out.println(str);
        }
    }
}
