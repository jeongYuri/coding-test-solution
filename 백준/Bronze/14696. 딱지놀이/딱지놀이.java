import java.io.*;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int n = Integer.parseInt(br.readLine());
		for(int i = 0;i<n;i++){
			int[]a = new int[5];
			int[]b = new int[5];

			StringTokenizer st = new StringTokenizer(br.readLine());
			int aNum = Integer.parseInt(st.nextToken());
			for(int j = 0;j<aNum;j++){
				a[Integer.parseInt(st.nextToken())]++;
			}
			st = new StringTokenizer(br.readLine());
			int bNum = Integer.parseInt(st.nextToken());
			for(int j = 0;j<bNum;j++){
				b[Integer.parseInt(st.nextToken())]++;
			}

			char res = 'D';
			for(int j = 4;j>=1;j--){
				if(a[j]>b[j]){
					res ='A';
					break;
				}else if(a[j]<b[j]){
					res = 'B';
					break;
				}
			}
			System.out.println(res);
		}

	}
       

    
}