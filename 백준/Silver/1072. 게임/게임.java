import java.util.Scanner;
import java.io.IOException;

public class Main {

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        long x = sc.nextInt();
        long y = sc.nextInt();
        long z = ((y*100)/x);
        if(z>98){
          System.out.println("-1");
          return;
        }
        long start = 0;
        long end = x;
        long res = -1;
        while(start<end){
          long mid = (start+end)/2;
          if((y+mid)*100/(x+mid) != z){
               end = mid;
          }else{
               start = mid+1;
               res = mid+1;
          }
        }
        System.out.println(res);   
    }
}
