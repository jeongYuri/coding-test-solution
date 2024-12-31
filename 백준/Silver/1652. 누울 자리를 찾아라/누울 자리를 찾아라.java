import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<String> board = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            board.add(br.readLine());
        }
        int[]ans = new int[2];
        for(int i=0;i<n;i++){
            int r = 0, c = 0;
            for(int j=0;j<n;j++){
                if(board.get(i).charAt(j)=='.'){
                    r+=1;
                }else{
                    r=0;
                }if(r==2){
                    ans[0] +=1;
                }if(board.get(j).charAt(i)=='.'){
                    c+=1;
                }else{
                    c = 0;
                }if(c==2){
                    ans[1]+=1;
                }
            }
        }
        System.out.println(ans[0]+" "+ans[1]);
    }
    
}
