import java.io.*;
import java.util.*;

public class Main {
    //모음 리스트트
    static final Set<Character> mo = new HashSet<>(Arrays.asList('a','e','i','o','u'));
    public static boolean check(String password){
        //모음이 최소 하나인지 확인인
        boolean hasMo = false;
        for(char ch: password.toCharArray()){
            if(mo.contains(ch)){
                hasMo = true;
                break;
            }
        }
        if(!hasMo) return false;

        //연속된 모음 3개 또는 자음 3개 확인인
        for(int i=0;i<password.length()-2;i++){
            boolean allMo = mo.contains(password.charAt(i)) &&
                            mo.contains(password.charAt(i+1))&&
                            mo.contains(password.charAt(i+2));
            boolean allJa = !mo.contains(password.charAt(i))&&
                            !mo.contains(password.charAt(i+1))&&
                            !mo.contains(password.charAt(i+2));
            if(allMo || allJa){
                return false;
            }
        }
        //같은 글자가 연속 2번 나오는지 확인 !e와 o는 예외외
        for(int i=0;i<password.length()-1;i++){
            if(password.charAt(i)==password.charAt(i+1)&&
            password.charAt(i)!='e'&&password.charAt(i)!='o'){
                return false;
            }
        }
        return true;
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while(true){
            String password = br.readLine().trim();
            if(password.equals("end"))break;
            if(check(password)){
                System.out.println("<"+password+"> is acceptable. ");
            }else{
                
                System.out.println("<"+password+"> is not acceptable. ");
            }
        }
        
    }
}
