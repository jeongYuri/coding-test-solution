import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        char[] wheel = new char[n];
        Arrays.fill(wheel,'?');

        int currentPos = 0;
        boolean isPossible = true;

        for(int i = 0;i<k;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            char b = st.nextToken().charAt(0);
          
            currentPos = (currentPos-a)%n;
            if(currentPos<0) currentPos += n;

            if(wheel[currentPos]=='?'){
                wheel[currentPos] = b;
            }else if(wheel[currentPos]!=b){
                isPossible = false;
                break;
            }
        }

        Set<Character> seen = new HashSet<>();
        for(char ch: wheel){
            if(ch!='?' && !seen.add(ch)){
                isPossible = false;
                break;
            }
        }
        if(!isPossible){
            System.out.println("!");
        }else{
            StringBuilder sb = new StringBuilder();
            for(int i = 0;i<n;i++){
                int idx = (currentPos+i)%n;
                sb.append(wheel[idx]);
            }
            System.out.println(sb);
        }



       
    }
}