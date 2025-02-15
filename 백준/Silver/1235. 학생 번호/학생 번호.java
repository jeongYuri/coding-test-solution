import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String[] students = new String[n];

        for(int i = 0;i<n;i++){
            students[i] = br.readLine().trim();
        }
        int end = 1;
        while (true) {
            Set<String> res = new HashSet<>();
            for(String student: students){
                int len = student.length();
                res.add(student.substring(Math.max(0,len-end)));
            }
            if(res.size()==n){
                System.out.println(end);
                break;
            }
            end++;
            
        }
    }
}
