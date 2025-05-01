import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int a = Integer.parseInt(st.nextToken());
		int b = Integer.parseInt(st.nextToken());

		int reverseA = reverse(a);
		int reverseB = reverse(b);

		System.out.println(Math.max(reverseA,reverseB));

	} 
	static int reverse(int num){
		int reversed = 0;
		while(num!=0){
			int digit = num %10;
			reversed = reversed *10+digit;
			num/=10;
		}
		return reversed;
	}
    
}