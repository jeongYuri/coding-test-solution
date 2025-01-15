import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int x = Integer.parseInt(st.nextToken());
        int y = Integer.parseInt(st.nextToken());
        List<Integer> x_cut = new ArrayList<>();
        List<Integer> y_cut = new ArrayList<>();
        x_cut.add(0);
        x_cut.add(x);
        y_cut.add(0);
        y_cut.add(y);
        int k = Integer.parseInt(br.readLine());
        
        for(int i=0;i<k;i++){
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            if(a==0){
                y_cut.add(b);
            }else{
                x_cut.add(b);
            }
        }
        Collections.sort(x_cut);
        Collections.sort(y_cut);
        int maxX = 0;
        for(int i=0;i<x_cut.size()-1;i++){
            int diff = x_cut.get(i+1)-x_cut.get(i);
            if(diff>maxX){
                maxX = diff;
            }
        }
        int maxY = 0;
        for(int i = 0; i < y_cut.size() - 1; i++) {
            int diff = y_cut.get(i+1) - y_cut.get(i);
            if(diff > maxY) {
                maxY = diff;
            }
        }

        System.out.println(maxX * maxY);
        
    }

    }

