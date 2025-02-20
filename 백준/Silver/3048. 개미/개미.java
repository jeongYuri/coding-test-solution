import java.io.*;
import java.util.*;

public class Main {
    static int n;
    static char[][] cookie;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n1 = Integer.parseInt(st.nextToken()); // 첫 번째 그룹 개미 수
        int n2 = Integer.parseInt(st.nextToken());

        String group1 = br.readLine(); // 첫 번째 개미 그룹 (오른쪽 이동)
        String group2 = br.readLine(); //두 번째개미 그룹
        int time = Integer.parseInt(br.readLine());
        
        StringBuilder sb  = new StringBuilder(); //첫번째 그룹 뒤집어서 저장~~
        sb.append(new StringBuilder(group1).reverse()); 
        sb.append(group2);
        char[] ants = sb.toString().toCharArray(); //개미들 문자 배열로 변환하기기
        

        for(int t =0;t<time;t++){
            for(int i = 0;i<ants.length-1;i++){
                if(group1.contains(String.valueOf(ants[i]))&&group2.contains(String.valueOf(ants[i+1]))){
                    char temp = ants[i];
                    ants[i] = ants[i+1];
                    ants[i+1] = temp;

                    i++;
                }
            }
        }
        System.out.println(new String(ants));   
        }
    }

