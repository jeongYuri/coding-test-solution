import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;

public class Main{
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int k = Integer.parseInt(br.readLine());
        List<int[]> info = new ArrayList<>();
        for(int i=0;i<6;i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            int d = Integer.parseInt(st.nextToken());
            int l = Integer.parseInt(st.nextToken());
            info.add(new int[]{d,l});
        }
        int maxWidth = 0;
        int maxHeight = 0;
        int widthIdx = 0;
        int heightIdx = 0;

        for(int i=0;i<6;i++){
            int[] arr = info.get(i);
            int d = arr[0];
            int length = arr[1];
            if(d==1 || d==2){
                if(length>maxWidth){
                    maxWidth = length;
                    widthIdx = i;
                }
            }else{
                if(d==3||d==4){
                    if(length>maxHeight){
                        maxHeight = length;
                        heightIdx = i;
                    }
                }
            }
        }
        int smallWidth = info.get((widthIdx + 3) % 6)[1];
        int smallHeight = info.get((heightIdx + 3) % 6)[1];

        int big_area  = maxWidth*maxHeight;
        int small_area = smallWidth * smallHeight;

        int res = (big_area-small_area)*k;
        System.out.println(res);
    }
}
