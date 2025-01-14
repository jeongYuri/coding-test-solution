import java.util.*;
import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        int[] order = new int[k];
        st = new StringTokenizer(br.readLine());
        for(int i=0;i<k;i++){
            order[i] = Integer.parseInt(st.nextToken());
        }
        List<Integer> plug  = new ArrayList<>();
        int res = 0;

        for(int i=0;i<k;i++){
            int current = order[i];
            if(plug.contains(current)){
                continue;
            }
            if(plug.size()<n){
                plug.add(current);
                continue;
            }
            int farthest = -1;
            int delete = -1;
            for(int j=0;j<plug.size();j++){
                int device = plug.get(j);
                int next;
                next = finduse(order,i+1,device);
                if(next==-1){
                    delete = j;
                    break;
                }
                if(next>farthest){
                    farthest = next;
                    delete = j;
                }
            }
            plug.set(delete, current);
            res++;

        }
        System.out.println(res);
    }
    private static int finduse(int[] order, int start, int device){
        for(int i=start;i<order.length;i++){
            if(order[i]==device){
                return i;
            }
        }
        return -1;
    }

    }

