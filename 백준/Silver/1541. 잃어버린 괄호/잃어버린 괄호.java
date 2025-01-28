import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        Scanner sc = new Scanner(System.in);
        String input = sc.nextLine();

        String[] parts = input.split("-");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            String[] subParts = parts[i].split("\\+");
            int sum = 0;
            for (String num : subParts) {
                sum += Integer.parseInt(num); 
            }
            nums[i] = sum; 
        }

        int result = nums[0];
        for (int i = 1; i < nums.length; i++) {
            result -= nums[i];
        }

        System.out.println(result);
        sc.close();
    }
}
