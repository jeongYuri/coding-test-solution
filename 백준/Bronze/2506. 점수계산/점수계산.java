import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt(); 
        sc.nextLine(); 

        int ans = 0;
        int score = 0;
        
        String nums = sc.nextLine(); 
        String[] numberStrings = nums.split(" ");
        
        int[] scores = new int[n];
        
        for (int i = 0; i < n; i++) {
            scores[i] = Integer.parseInt(numberStrings[i]);
        }
        
        for (int i = 0; i < n; i++) {
            if (scores[i] == 1) {
                score += 1;
                ans += score;
            } else {
                score = 0;
            }
        }
        
        System.out.println(ans);
    }
}