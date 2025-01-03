import java.util.*;
import java.io.*;

public class Main{
    static char[] res;
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input;

        while((input =br.readLine())!=null && !input.isEmpty()){
            int n = Integer.parseInt(input.trim());
            int size = (int) Math.pow(3,n);
            res = new char[size];
            for(int i=0;i<size;i++){
                res[i] = '-';
            }
            cut(0,size);
            System.out.println(new String(res));
            }
        }
        static void cut(int start, int length){
            if(length==1){
                return ;
            }
            int third = length/3;
            //중간 부분 공백 처리리
            for(int i=start+third;i<start+2*third;i++){
                res[i] = ' ';
            }
            //재귀 호출
            cut(start, third);//왼쪽
            cut(start+2*third,third);//오른쪽
        }
    }
