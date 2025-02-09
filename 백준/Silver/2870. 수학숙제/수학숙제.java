import java.io.*;
import java.util.*;
import java.util.regex.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());
        List<BigInteger> numbers = new ArrayList<>();
        Pattern pattern = Pattern.compile("\\d+");

        for(int t = 0;t<tc;t++){
            String word = br.readLine().trim();
            Matcher matcher = pattern.matcher(word);
            while(matcher.find()){
                BigInteger num = new BigInteger(matcher.group());
                numbers.add(num);
            }
            
        }
        Collections.sort(numbers);
        StringBuilder sb = new StringBuilder();
        for(BigInteger num : numbers){
            sb.append(num.toString()).append("\n");
        }
        System.out.println(sb);
        }
           
}

