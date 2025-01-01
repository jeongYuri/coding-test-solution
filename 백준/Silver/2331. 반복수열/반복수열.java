import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = sc.nextInt();
        int p = sc.nextInt();
        List<Integer> d = new ArrayList<>();
        d.add(a);

        while(true){
            int current = d.get(d.size()-1);
            int newvalue = 0;

            while(current>0){
                int digit = current %10;
                newvalue += Math.pow(digit,(double)p);
                current /=10;
            }
            if (d.contains(newvalue)) {
                System.out.println(d.indexOf(newvalue));
                break;
            }

            d.add(newvalue); 
        }
    }
}
    

