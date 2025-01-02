import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.util.*;
public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int taesu = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());
        if(n==0){
            System.out.println(1);
            return;
        } 
        st = new StringTokenizer(br.readLine());
        List<Integer> scores = new ArrayList<>();
        for(int i=0;i<n;i++){
            scores.add(Integer.parseInt(st.nextToken()));
        }
        scores.add(taesu);
        Collections.sort(scores, Collections.reverseOrder());
        int res = rank(scores,taesu);
        if(n==p && taesu<=scores.get(scores.size()-1)){
            System.out.println(-1);
        }else{
            System.out.println(res);
        }
    }
       
            
    private static int rank(List<Integer>scores, int taesu){
        Map<Integer,Integer> ranks = new HashMap<>();
        int rank =1;
        for(int score:scores){
            if(!ranks.containsKey(score)){
                ranks.put(score,rank);//새로운 점수일 경우 순위 부여
            }
            rank++;
        }
        return ranks.get(taesu);
    }
}

    

