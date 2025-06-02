import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int n = Integer.parseInt(st.nextToken());
		int k = Integer.parseInt(st.nextToken());
		
		List<Integer> list = new ArrayList<>();
		List<Integer> res = new ArrayList<>();
		int idx = 0;
		for(int i = 1;i<=n;i++){
			list.add(i);
		}
		int cc = 0;
		while(!list.isEmpty()){
			idx = (idx+k-1)%list.size();
			res.add(list.remove(idx));
		}

		System.out.print("<");
		for(int i = 0;i<res.size();i++){
			System.out.print(res.get(i));
			if(i!=res.size()-1){
				System.out.print(", ");
			}
		}
		System.out.print(">");
	}
	
} 
	   
