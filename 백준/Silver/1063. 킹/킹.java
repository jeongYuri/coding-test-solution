import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        String king = st.nextToken();  // 킹의 위치
        String stone = st.nextToken(); // 돌의 위치
        int n = Integer.parseInt(st.nextToken()); // 명령 개수

        int kx = king.charAt(0)-'A'+1;
        int ky = king.charAt(1)-'0';
        int sx = stone.charAt(0)-'A'+1;
        int sy = stone.charAt(1)-'0';

        HashMap<String, int[]> moveDict = new HashMap<>();
        moveDict.put("R", new int[]{1, 0});
        moveDict.put("L", new int[]{-1, 0});
        moveDict.put("B", new int[]{0, -1});
        moveDict.put("T", new int[]{0, 1});
        moveDict.put("RT", new int[]{1, 1});
        moveDict.put("LT", new int[]{-1, 1});
        moveDict.put("RB", new int[]{1, -1});
        moveDict.put("LB", new int[]{-1, -1});

        for(int i = 0;i<n;i++){
            String command = br.readLine();
            if(moveDict.containsKey(command)){
                int dx = moveDict.get(command)[0];
                int dy = moveDict.get(command)[1];
                
                int nkx = kx+dx, nky = ky+dy;
                
                if(nkx==sx && nky == sy){
                    int nsx = sx+dx, nsy= sy+dy;
                    if(1<=nsx && nsx<=8 && 1<=nsy && nsy<=8){
                        kx = nkx;
                        ky = nky;
                        sx = nsx;
                        sy = nsy;

                    }
            }else{
                if (1 <= nkx && nkx <= 8 && 1 <= nky && nky <= 8) {
                    kx = nkx;
                    ky = nky;
                }
            }
        }
    }
        System.out.println((char) (kx + 'A' - 1) + "" + ky);
        System.out.println((char) (sx + 'A' - 1) + "" + sy);
        

    }
   
}
