import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());

		for(int i =n;i>=0;i--){
			if(check(i)){
				System.out.println(i);
				break;
			}
		}
    }
	public static boolean check(int num){
		while(num>0){
			int digit = num %10;//마지막 자리 숫자 확인
			if(digit!=4 && digit!=7){
				return false;
			}
			num/=10;
		}
		return true;

	}
       

    
}