import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());
    
        for(int i = 0;i<t;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int x = Integer.parseInt(st.nextToken());
            int y = Integer.parseInt(st.nextToken());
            
            int d = y-x;

            int max = (int)Math.sqrt(d);

            if(max==Math.sqrt(d)){
                System.out.println(max*2-1);
            }else if(d<=max*max+max){
                System.out.println(max*2);
            }
            else{
                System.out.println(max*2+1);
            }
            }
        }     
        }
    
