import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    static int n, k , maxValue = 0;
    static List<Integer> numbers = new ArrayList<>();
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        k = sc.nextInt();

        for(int i=0;i<k;i++){
            numbers.add(sc.nextInt());
        }
        sc.close();

        Collections.sort(numbers, Collections.reverseOrder());
        int length = String.valueOf(n).length();
        while(length>0){
            generateNumbers(0,length,"");
            if(maxValue>0) break;
            length--;
        }
        System.out.println(maxValue);
    }
    static void generateNumbers(int depth, int targetLength, String current){
        if(depth==targetLength){
            int num = Integer.parseInt(current);
            if(num<=n){
                maxValue = Math.max(maxValue, num);
            }
            return ;
        }
        for(int num: numbers){
            generateNumbers(depth+1, targetLength, current+num);
        }
    }
}
