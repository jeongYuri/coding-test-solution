import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long n = sc.nextLong();
        long total = 0;
        int cnt = 0;
        while (true) {
            cnt +=1;
            total+=cnt;
            if(total>n){
                break;
            }
        }
        System.out.println(cnt-1);
        sc.close();
    }
}