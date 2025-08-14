import java.io.*;
import java.util.*;

public class Main{
	static int count  = 0;
    public static void main(String[] args)throws IOException{
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int t = Integer.parseInt(br.readLine());
		StringBuilder sb = new StringBuilder();
		for(int i = 0;i<t;i++){
			String S = br.readLine();
			count = 0;
			sb.append(isPalindrome(S)).append(" ").append(count).append("\n");

		}
        br.close();
		System.out.println(sb);
    }
	public static int recursion(String s, int l, int r){
		count++;
        if(l >= r) return 1;
        else if(s.charAt(l) != s.charAt(r)) return 0;
        else return recursion(s, l+1, r-1);
    }
    public static int isPalindrome(String s){
        return recursion(s, 0, s.length()-1);
    }
}
	   
