import java.util.*;
import java.io.*;
import java.lang.reflect.Array;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int a = Integer.parseInt(st.nextToken());
        int b = Integer.parseInt(st.nextToken());

        int n  = Integer.parseInt(br.readLine());
        int[] buttons = new int[n];
        for(int i=0;i<n;i++){
            buttons[i] = Integer.parseInt(br.readLine());
        }

        int minClick = Math.abs(b-a);
        for(int button : buttons){
            int click = Math.abs(b-button)+1;
            minClick = Math.min(minClick, click);
        }
        System.out.println(minClick);
    }
}

