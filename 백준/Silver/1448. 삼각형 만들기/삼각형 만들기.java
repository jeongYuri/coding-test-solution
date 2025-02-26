import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] straws = new int[n];

        for(int i = 0;i<n;i++){
            straws[i] = Integer.parseInt(br.readLine());
        }

        Arrays.sort(straws);

        for(int i = n-1;i>=2;i--){
            if(straws[i]<straws[i-1]+straws[i-2]){
                System.out.println(straws[i] + straws[i - 1] + straws[i - 2]);
                return;
        }
    }
        System.out.println(-1);
    }
    }
