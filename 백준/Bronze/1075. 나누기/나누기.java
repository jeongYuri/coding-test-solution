import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int f = sc.nextInt();
        int base = (n/100)*100;
        int res = 0;
        for(int i=0;i<100;i++){
            if((base+i)%f==0){
                res = i;
                break;
            }
        }
        System.out.printf("%02d",res);
    }
}