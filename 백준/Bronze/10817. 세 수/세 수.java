import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String []inputs = br.readLine().split(" ");
		int [] arrs = new int[inputs.length];
		for(int i = 0;i<inputs.length;i++){
			arrs[i] = Integer.parseInt(inputs[i]);
		}
		Arrays.sort(arrs);
		System.out.println(arrs[1]);


	}
       

    
}