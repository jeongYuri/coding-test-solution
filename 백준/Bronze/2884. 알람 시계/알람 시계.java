import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int h = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        m-=45;
        if(m<0){
            m+= 60;
            h--;
            if(h<0)h= 23;
        }
        System.out.println(h + " " + m);
    }
}
    
