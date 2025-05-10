import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        
        for (int i = 0; i < t; i++) {
            String a = sc.next();
            String b = sc.next();
            
            char[] arrA = a.toCharArray();
            char[] arrB = b.toCharArray();
            
            Arrays.sort(arrA);
            Arrays.sort(arrB);
            
            if (Arrays.equals(arrA, arrB)) {
                System.out.printf("%s & %s are anagrams.%n", a, b);
            } else {
                System.out.printf("%s & %s are NOT anagrams.%n", a, b);
            }
        }
        sc.close();
    }
}
