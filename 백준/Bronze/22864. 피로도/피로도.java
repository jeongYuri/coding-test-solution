import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int a = Integer.parseInt(input[0]);
        int b = Integer.parseInt(input[1]);
        int c = Integer.parseInt(input[2]);
        int m = Integer.parseInt(input[3]);
        int work = 0;
        int fatigue = 0;
        for(int i=0;i<24;i++){
            if(fatigue+a <=m){
                work+=b;
                fatigue+=a;
            }else{
                fatigue = Math.max(0,fatigue-c);
            }
        }
        System.out.println(work);
        }
    }
