import java.io.*;
import java.util.*;
import java.util.Comparator;
import java.util.PriorityQueue;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String s = br.readLine().trim();
        String t = br.readLine().trim();

        int lcmLength = lcm(s.length(),t.length());

        StringBuilder sRepeated = new StringBuilder();
        StringBuilder tRepeated = new StringBuilder();

        for(int i=0;i<lcmLength/s.length();i++){
            sRepeated.append(s);
        }
        for(int i=0;i<lcmLength/t.length();i++){
            tRepeated.append(t);
        }

        if(sRepeated.toString().equals(tRepeated.toString())){
            System.out.println(1);
        }else{
            System.out.println(0);
        }

    }
    public static int lcm(int a, int b){
        return a*(b/gcd(a,b));
    }
    public static int gcd(int a, int b){
        while(b!=0){
            int temp = b;
            b = a%b;
            a = temp;
        }
        return a;
    }
}