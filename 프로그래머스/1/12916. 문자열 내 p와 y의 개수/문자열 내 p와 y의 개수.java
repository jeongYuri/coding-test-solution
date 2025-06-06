class Solution {
    boolean solution(String s) {
        boolean answer = true;

        s = s.toLowerCase();//소문자 변환
        int pCount = 0;
        int yCount = 0;
        
        for(int i = 0;i<s.length();i++){
            char ch = s.charAt(i);
            if(ch=='p'){
                pCount++;
            }else if(ch=='y'){
                yCount++;
            }
        }
        return pCount==yCount;
    }
}