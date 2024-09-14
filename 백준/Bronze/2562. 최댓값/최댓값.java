import java.util.Arrays;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
            Scanner sc = new Scanner(System.in);
            int []nums = new int[9];
            int max = 0;
            int maxIndex = 0;
            for (int i=0;i<9;i++){
                nums[i] = sc.nextInt();
                if(nums[i]>max){
                    max = nums[i];
                    maxIndex = i+1;
                }
            }
            System.out.println(max);
            System.out.print(maxIndex);
            sc.close();
    }
    
}