import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        List<Integer> nums = new ArrayList<>();
        while(n>0){
            nums.add(0,n%10);
            n/=10; //자릿수 줄이기?
        }
        Collections.sort(nums, Collections.reverseOrder());
        for(int nd:nums){
            System.out.print(nd);
        }

    }
}