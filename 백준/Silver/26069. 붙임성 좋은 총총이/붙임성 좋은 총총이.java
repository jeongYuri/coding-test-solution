import java.io.BufferedReader;
import java.io.IOException;
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt(); 
        sc.nextLine(); 
        Set<String> meet = new HashSet<>(); 

        for (int i = 0; i < n; i++) {
            String[] input = sc.nextLine().split(" ");
            String a = input[0];
            String b = input[1];

            
            if (a.equals("ChongChong") || b.equals("ChongChong")) {
                meet.add(a);
                meet.add(b);
            }
            if (meet.contains(a) || meet.contains(b)) {
                meet.add(a);
                meet.add(b);
            }
        }


        System.out.println(meet.size());
    }
}
    

