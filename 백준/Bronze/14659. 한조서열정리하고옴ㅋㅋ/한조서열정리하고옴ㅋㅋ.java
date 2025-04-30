import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		String []inputs = br.readLine().split(" ");
		int [] m = new int[n];
		for(int i = 0;i<n;i++){
			m[i] = Integer.parseInt(inputs[i]);
		}
		
		int max = 0;
		for(int i = 0;i<n;i++){
			int cnt = 0;
			for(int j =i+1;j<n;j++){
				if(m[i]>m[j]) cnt ++;
				else break;
			}
			max = Math.max(max, cnt);
		}
		System.out.println(max);

	}
       

    
}