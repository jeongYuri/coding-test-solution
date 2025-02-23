import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String pattern = br.readLine().trim();

        String[] parts = pattern.split("\\*",2);
        String prefix = parts[0];
        String suffix = parts[1];

        StringBuilder sb = new StringBuilder();
        for(int i = 0;i<n;i++){
            String file = br.readLine().trim();

            if(file.length()<prefix.length() + suffix.length()){
                sb.append("NE\n");
            }else if(file.startsWith(prefix)&&file.endsWith(suffix)){
                sb.append("DA\n");
            }else{
                sb.append("NE\n");
            }
        }
        System.out.println(sb.toString());
    }
}
