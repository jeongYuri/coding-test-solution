public class Solution {
    public int[] solution(int[] sequence, int k) {
        int start = 0, end = 0;
        int sum = 0;
        int minLength = Integer.MAX_VALUE;
        int[] answer = new int[2];

        while (end < sequence.length) {
            sum += sequence[end];

            while (sum >= k) {
                if (sum == k && (end - start + 1) < minLength) {
                    minLength = end - start + 1;
                    answer[0] = start;
                    answer[1] = end;
                }
                sum -= sequence[start];
                start++;
            }
            end++;
        }
        return answer;
    }
}