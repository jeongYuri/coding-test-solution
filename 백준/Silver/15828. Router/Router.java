import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        Queue<Integer> router = new LinkedList<>();

        while(true){
            int info = Integer.parseInt(br.readLine());
            if(info ==-1){
                break;
            }
            if(info > 0){
                if(router.size()<n){
                    router.offer(info);
                }
            }else if(info == 0){
                if(!router.isEmpty()){
                    router.poll();
                }
            }
        }
        if(router.isEmpty()){
            System.out.println("empty");
        }else{
            StringBuilder sb = new StringBuilder();
            for(int packet:router){
                sb.append(packet).append(" ");
            }System.out.println(sb.toString().trim());
        }

    }
}
