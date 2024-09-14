import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int n = sc.nextInt();
            sc.nextLine();
            String word = sc.nextLine();
            int [] nums = new int[n];
            
            for(int i=0;i<n;i++){
                nums[i] = Character.getNumericValue(word.charAt(i));
            }
            int sum = 0;
            for(int num : nums){
                sum += num;
            }
            System.out.println(sum);
            sc.close();
    }

}
