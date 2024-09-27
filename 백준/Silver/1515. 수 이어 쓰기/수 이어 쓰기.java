import java.util.*;
import java.io.*;
public class Main{
    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String remain =  br.readLine().trim();
        int n = 0;
        int pt = 0;
        while(true){
            n++;
            String currentN = String.valueOf(n);
            for(int i=0;i<currentN.length();i++){
                if(pt<remain.length() && currentN.charAt(i) == remain.charAt(pt)){
                    pt++;
                }
                if(pt == remain.length()){
                    System.out.println(n);
                    return;
                }
            }
        }
        }

    }
