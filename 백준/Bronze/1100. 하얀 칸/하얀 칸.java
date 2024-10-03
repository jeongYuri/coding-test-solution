import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        char[][]chess = new char[8][8];
        
        for(int i=0;i<8;i++){
            String line = sc.next();
            for(int j=0;j<8;j++){
                chess[i][j] = line.charAt(j);
            }
        }
        int cnt = 0;
        for(int i=0;i<8;i++){
            for(int j=0;j<8;j++){
                if ((i + j) % 2 == 0 && chess[i][j] == 'F') {
                    cnt += 1;
                }
            }
        }
    System.out.println(cnt);
    }
}