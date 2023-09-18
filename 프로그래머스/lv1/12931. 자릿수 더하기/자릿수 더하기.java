import java.util.*;

public class Solution {
    public int solution(int n) {
        int answer = 0;
        ArrayList <Integer> nums = new ArrayList<>();
        while(n>0){
            nums.add(n%10);
            n/=10;
        }
        for(int num : nums){
            answer +=num;
        }
        return answer;
    }
}