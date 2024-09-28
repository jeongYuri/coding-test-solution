import java.io.*;
import java.util.*;
import java.util.regex.*;;
public class Main{
    public static void main(String[] args)throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();

        Pattern pattern = Pattern.compile("(0+|1+)"); //정규 표현식으로 그룹
        Matcher matcher = pattern.matcher(s);

        Map<Integer, Integer> cnt = new HashMap<>();
        cnt.put(0,0);
        cnt.put(1,0);

        while(matcher.find()){
            String g = matcher.group(); // 매칭된 그룹 카운트하려는 while
            if(g.contains("1")){
                cnt.put(1,cnt.get(1)+1);
            }else{
                cnt.put(0,cnt.get(0)+1);
            }
        }
    System.out.println(Math.min(cnt.get(0),cnt.get(1)));
    }
}
