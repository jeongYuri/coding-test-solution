import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String line;
        while((line=br.readLine())!= null && !line.trim().isEmpty()){
            String[] input = line.trim().split(" ");
            String s = input[0];
            String t = input[1];
            int idx = 0;
            for(char c:t.toCharArray()){
                if(idx<s.length() && c==s.charAt(idx)){
                    idx ++;
                }
            }
            System.out.println(idx==s.length()?"Yes":"No");
        }
    }
}