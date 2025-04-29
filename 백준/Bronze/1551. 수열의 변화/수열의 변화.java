import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		String [] input = br.readLine().split(",");
		int [] arr = new int[n];
		for(int i = 0;i<n;i++){
			arr[i] = Integer.parseInt(input[i]);
		}
		for(int step = 0;step<k;step++){
			int[]next = new int[arr.length-1];
			for(int i = 0;i<arr.length-1;i++){
				next[i] = arr[i+1]-arr[i];
		}
		arr = next;
		}
	
		for(int i = 0;i<arr.length;i++){
			if(i>0) System.out.print(",");
			System.out.print(arr[i]);
		}

	}
       

    
}